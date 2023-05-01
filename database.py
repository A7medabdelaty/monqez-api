from schema import User as userSchema
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://AhmedAbdelaty:root@localhost:5432/monqez"

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    'postgresql+psycopg2://ahmedabdelaty:knHIvV8RFhueOuuD8cWFvmA8WWCpFfEY@dpg-cgrgmijk9u56e3n08qq0-a.oregon-postgres.render.com:5432/monqez_db')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

SessionLocal.configure(bind=engine)
