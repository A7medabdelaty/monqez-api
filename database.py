from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://AhmedAbdelaty:root@localhost:5432/monqez"

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    'postgresql+psycopg2://ahmedabdelaty:VCaT1U2ltWTSduBGIXR2cw3y5kCVxg0I@dpg-cik1rr5ph6euh7j98kn0-a.oregon-postgres.render.com:5432/monqez_5qgl')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

SessionLocal.configure(bind=engine)
