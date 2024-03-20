# from sqlalchemy.orm import Session
from ..model import user

# def get_item(db: Session, item_id: int):
def get_item(item_id: int):
    # return db.query(user.User).filter(user.User.id == item_id).first()
    return {"user": "hello"}
