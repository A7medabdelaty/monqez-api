from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from schema import User as userSchema

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

    def get_userModel(user: userSchema):
        return User(id=user.id, first_name=user.first_name, last_name=user.last_name,
                    age=user.age, national_id=user.national_id, email=user.email, gender=user.gender, city=user.city,
                    str_address=user.str_address,
                    lat=user.lat,
                    long=user.long,
                    phone_1=user.phone_1,
                    phone_2=user.phone_2,
                    icd_code=user.icd_code,
                    blood_type=user.blood_type,
                    gastritis=user.gastritis,
                    liver_cirrhosis=user.liver_cirrhosis,
                    epidemic_hepatitis=user.epidemic_hepatitis,
                    hepatic_failure=user.hepatic_failure,
                    renal_failure=user.renal_failure,
                    gastric_ulcer=user.gastric_ulcer,
                    diabetes=user.diabetes,
                    tuberculosis=user.tuberculosis,
                    cancer=user.cancer,)
