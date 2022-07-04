import unittest

from fastapi.testclient import TestClient
from fastapi import FastAPI
from router.v0.api import router

app = FastAPI()
app.include_router(router)
client = TestClient(app)


class TestConfig(unittest.TestCase):
    def test_Save_facebook_page_posts(self):
        response = client.post(
            "pages/fbPages/beINSPORTS/posts",
            json={
                "postNumber": "10",
            },
        )
        assert response.status_code == 200

    def test_Save_facebook_page_posts_wrong_page_name(self):
        response = client.post(
            "pages/fbPages/ghf/posts",
            json={
                "postNumber": "10",
            },
        )
        assert response.status_code == 404
        assert response.json() == {"detail": "page or posts not found"}


