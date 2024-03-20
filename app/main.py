from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy.orm import Session
import os

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

from .model.user import Base
from .schemas.user import UserResponse
from .database.settings import SessionLocal, engine
from .database.connection import get_db
from .controller.user import get_item

Base.metadata.create_all(bind=engine)

app = FastAPI()

# app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

@app.get("/userrr", response_model=UserResponse)
# def read_item(item_id: int, db: Session = Depends(get_db)):
def read_item(item_id: int):
    item = get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item