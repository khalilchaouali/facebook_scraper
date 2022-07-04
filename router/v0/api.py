from fastapi import APIRouter
from router.v0 import extract_facebook_data

router = APIRouter()


router.include_router(extract_facebook_data.router, tags=["pages"], prefix="/pages")
