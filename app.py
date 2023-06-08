from pydantic import BaseModel
import random
from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from typing import List
from schema import User as userSchema
import uvicorn
import Model.baseModel as Model

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return {
        "message": "to get the iamge's user, send post request on ./getuser and send the iamge with the base64 with it",
    }


@app.get("/users/", response_model=List[userSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users


class Image(BaseModel):
    data: str


@app.post("/addUser/")
def create_user(user: userSchema, db: Session = Depends(get_db)):
    db_user = User.get_userModel(user)
    try:
        db.add(db_user)
        db.commit()
        return {"message": "User created successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()


@app.delete("/deleteUser/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        db_user = db.query(User).filter(User.id == user_id).first()
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        db.delete(db_user)
        db.commit()
        return {"message": "User deleted successfully"}
    except HTTPException as e:
        db.rollback()
        raise HTTPException(status_code=404, detail=str(e.detail))
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()


@app.put("/updateUser/{user_id}")
def update_user(user_id: int, user: userSchema, db: Session = Depends(get_db)):
    try:
        db_user = db.query(User).filter(User.id == user_id).first()
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        db_user.id = user_id
        update_user_db(db_user, user)
        db.commit()
        return {"message": "User updated successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()


@app.get("/getUser/{user_id}", response_model=userSchema)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    return user


@app.post("/getUser", response_model=userSchema)
async def get_user_by_image(image: Image, db: Session = Depends(get_db)):
    model = Model.mymodel(image.data)
    person_id = model.prediction()
    print(person_id)
    user = db.query(User).filter(User.id == person_id).first()
    return user


def update_user_db(db_user: User, user: userSchema) -> User:
    db_user.first_name = user.first_name
    db_user.last_name = user.last_name
    db_user.age = user.age
    db_user.national_id = user.national_id
    db_user.email = user.email
    db_user.gender = user.gender
    db_user.city = user.city
    db_user.str_address = user.str_address
    db_user.lat = user.lat
    db_user.long = user.long
    db_user.phone_1 = user.phone_1
    db_user.phone_2 = user.phone_2
    db_user.icd_code = user.icd_code
    db_user.blood_type = user.blood_type
    db_user.gastritis = user.gastritis
    db_user.liver_cirrhosis = user.liver_cirrhosis
    db_user.epidemic_hepatitis = user.epidemic_hepatitis
    db_user.hepatic_failure = user.hepatic_failure
    db_user.renal_failure = user.renal_failure
    db_user.gastric_ulcer = user.gastric_ulcer
    db_user.diabetes = user.diabetes
    db_user.tuberculosis = user.tuberculosis
    db_user.cancer = user.cancer
    return db_user


if __name__ == '__main__':
    uvicorn.run("app:app", reload=True)

# .\scripts\activate
# uvicorn app:app --reload
