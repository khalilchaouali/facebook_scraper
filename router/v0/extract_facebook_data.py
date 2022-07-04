from fastapi import APIRouter, HTTPException, Body
from starlette.status import HTTP_400_BAD_REQUEST
from models.fb_request_model import Body
from dependencies.extract_facebook_data import save_posts
router = APIRouter()


@router.post("/fbPages/{page_name}/posts")
def Save_facebook_page_posts(page_name: str, body: Body):
    return save_posts(page_name, body.postNumber.real)
