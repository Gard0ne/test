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


@app.post("/users/")
def create_user(name: str, email: EmailStr, date_of_birth: date, phone_number: str = None, db: Session = Depends(get_db)):
    db_user = models.User(name=name, email=email, date_of_birth=date_of_birth, phone_number=phone_number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user