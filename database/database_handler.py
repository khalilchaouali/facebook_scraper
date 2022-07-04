from datetime import datetime
from pymongo import MongoClient, UpdateOne
from bson.objectid import ObjectId
from common.config_utils import get_db_credentials


class DbHandler:
    """
    Classe that handles interaction with mongo DB (connection, storage, retrieval)
    """

    def __init__(self):
        self.config = get_db_credentials()
        full_uri = str("mongodb://" +
                       self.config["mongo_username"] +
                       ":" + self.config["mongo_password"] +
                       "@" + self.config["mongo_uri"] +
                       ":" + str(self.config["mongo_port"]) +
                       "/" + "?authSource=" +
                       self.config["mongo_auth_source"]
                       )
        db_name = self.config["db_name"]
        try:
            self.connection = MongoClient(full_uri)
            self.database = self.connection[db_name]
            self.pages_posts_collection = self.database[self.config["mongo_collection_fb_pages"]]
        except Exception as err:
            print("MonogoDB connexion failed. " + str(err))

    """
    Method that load posts in bulk into the facebook_pages collection.
    """

    def insert_posts(self, posts: list):
        operations = [UpdateOne({'post_id': post["post_id"]}, {'$set': {"data": post["data"]}}, upsert=True) for post in
                      posts]
        return self.pages_posts_collection.bulk_write(operations).bulk_api_result
