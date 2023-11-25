from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:qachonkelasan@Localhost/mydb", echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)


class User_chat(Base):
    __tablename__ = 'userchat'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    username = Column(String)
    created = Column(DateTime)


class User_message(Base):
    __tablename__ = 'usermessage'
    id = Column(Integer, primary_key=True)
    message_id = Column(Integer)
    colum_message = Column(String)
    created = Column(DateTime)


Base.metadata.create_all(engine)