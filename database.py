from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# database 환경 변수 설정

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@127.0.0.1:3306/ptn?charset=utf8"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# session = SessionLocal()
