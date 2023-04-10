import base64
from pydantic import BaseModel
import random
from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from typing import List
from schema import User as userSchema
import uvicorn

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return {"message": "Hello World"}


@app.get("/users/", response_model=List[userSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users


class Image(BaseModel):
    data: str


@app.post("/getUser", response_model=userSchema)
async def generate_random_number(image: Image, db: Session = Depends(get_db)):
    # Decode base64-encoded image data
    img_data = base64.b64decode(image.data)

    # Process image here (e.g. using OpenCV or Pillow)
    # ...

    rand_num = random.randint(1, 1000)
    user = db.query(User).filter(User.id == rand_num).first()
    return user

if __name__ == '__main__':
    uvicorn.run("app:app", reload=True)

# python3 -m venv .
# .\scripts\activate
# uvicorn app:app --reload
