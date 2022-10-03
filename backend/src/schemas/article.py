from datetime import datetime

from pydantic import BaseModel, Field


class Article(BaseModel):
    id: int = Field(example="1", description="Article id")
    title: str = Field(example="Title 001", description="Article title")
    content: str = Field(example="Content", description="Article content")
    created_at: datetime = Field(example="2022-03-04 12:23:48", description="Article created timestamp")
    updated_at: datetime = Field(example="2022-05-16 15:35:20", description="Article updated timestamp")

    class Config:
        orm_mode = True
