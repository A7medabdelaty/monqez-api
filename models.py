from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = "user_data"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    national_id = Column(String)
    email = Column(String)
    gender = Column(String)
    city = Column(String)
    str_address = Column(String)
    lat = Column(String)
    long = Column(String)
    phone_1 = Column(String)
    phone_2 = Column(String)
    icd_code = Column(String)
    blood_type = Column(String)
    gastritis = Column(String)
    liver_cirrhosis = Column(String)
    epidemic_hepatitis = Column(String)
    hepatic_failure = Column(String)
    renal_failure = Column(String)
    gastric_ulcer = Column(String)
    diabetes = Column(String)
    tuberculosis = Column(String)
    cancer = Column(String)
