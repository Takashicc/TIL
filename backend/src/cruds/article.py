from sqlalchemy.orm import Session

from ..models import models


def find_all_articles(db: Session):
    return db.query(models.Article).all()
