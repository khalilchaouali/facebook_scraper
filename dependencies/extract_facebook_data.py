import json
from facebook_page_scraper import Facebook_scraper

from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from database.database_handler import DbHandler
from fastapi import status

"""
Function that hundle the extraction of the bost details based on page ID and number of posts.
"""


def get_posts(page_name: str, posts_count: int):
    try:
        meta_ai = Facebook_scraper(page_name, posts_count)
        data = json.loads(meta_ai.scrap_to_json())
        posts = []
        for key, value in data.items():
            posts.append({"post_id": key, "data": value})
        return posts
    except:
        return []


"""
    class that load the extract posts in mongo database.
"""


def save_posts(page_name: str, posts_count: int):
    posts = get_posts(page_name, posts_count)
    db = DbHandler()
    if posts != []:
        return db.insert_posts(posts)
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=jsonable_encoder({"detail": "page or posts not found"}),
        )
