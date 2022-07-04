from pydantic import BaseModel, Field


class Body(BaseModel):
    postNumber: int = Field(gt=0, description="the number of posts")
