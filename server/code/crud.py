import schemas
import models
from sqlalchemy.orm import Session
from sqlalchemy import update

#Search by text and return 20 docs
def search_post_by_text(db: Session, search_text: str):
    result = db.query(models.Post) \
        .filter(models.Post.text.contains(search_text)) \
        .order_by(models.Post.created_date.desc()) \
        .limit(20) \
        .all()
    return result


#Delete text by ID
def delete_by_id(db: Session, id: int) -> bool:
    result = db.query(models.Post).filter(models.Post.id == id).delete()
    db.commit()
    return bool(result)