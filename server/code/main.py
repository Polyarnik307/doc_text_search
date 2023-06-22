# coding=utf-8
from datetime import datetime
import shutil
from typing import List, Union

import crud
import schemas
import models
import uvicorn
from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException, File, UploadFile, Form
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    version="1.0",
    title="Doc search",
    description="Doc text search",
)

#Connection with DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Search by text
@app.get("/posts/search")
def search_post(text: str, db: Session = Depends(get_db)):
    results_list = crud.search_post_by_text(db=db, search_text=text)
    return {"result": results_list}

#Delete doc dy ID
@app.delete("/posts/delete")
def remove_post(remove_item: schemas.PostRemoveItem, db: Session = Depends(get_db)):
    result = crud.delete_by_id(db=db, id=remove_item.id)
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=False, use_colors=True)