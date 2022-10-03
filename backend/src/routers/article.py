from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..cruds import article as article_crud
from ..models.db import get_db
from ..schemas import article as article_schema

router = APIRouter()


@router.get(
    "/articles",
    response_model=List[article_schema.Article],
)
def read_articles(db: Session = Depends(get_db)):
    return article_crud.find_all_articles(db)
