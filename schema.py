from pydantic import BaseModel

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    age:int
    national_id:str
    email: str
    gender: str
    city: str
    str_address: str
    lat: str
    long: str
    phone_1: str
    phone_2: str
    icd_code: str
    blood_type: str
    gastritis: str
    liver_cirrhosis: str
    epidemic_hepatitis: str
    hepatic_failure: str
    renal_failure: str
    gastric_ulcer: str
    diabetes: str
    tuberculosis: str
    cancer: str

    class Config:
        orm_mode = True
