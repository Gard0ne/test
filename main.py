from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database, schemas
from datetime import date
from pydantic import EmailStr

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
