from common import config_utils
import unittest


class TestConfig(unittest.TestCase):

    def test_get_batch_credentials(self):
        print("mongoDev")
        path = config_utils.get_db_credentials()
        print(path)
