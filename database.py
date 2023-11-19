from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, Table, String, DateTime, Sequence
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy_utils import drop_database
from sqlalchemy.sql import func
from sqlalchemy.orm import backref


db_host = "194.87.232.20"
Base = declarative_base()
engine = create_engine(f'postgresql+psycopg://postgres:postgres@{db_host}:6666/trydb', echo=False)


class User(Base):
    __tablename__ = "users"
    tg_login = Column(String, primary_key=True)
    password = Column(String)
    discription = Column(String)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


HOBBY_TABLE_ID = Sequence('table_id_seq', start=10)
class Hobby(Base):
    __tablename__ = "hobbies"
    id = Column(Integer, HOBBY_TABLE_ID, primary_key=True, server_default=HOBBY_TABLE_ID.next_value())
    name = Column(String)
    discription = Column(String)
    avatar_link = Column(String)
    chat_id = Column(String)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


GROUP_TABLE_ID = Sequence('table_id_seq', start=10)
class Groups(Base):
    __tablename__ = "groups"
    id = Column(Integer, GROUP_TABLE_ID, primary_key=True, server_default=GROUP_TABLE_ID.next_value())
    id_hobby = Column(Integer)
    tg_login = Column(String)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


RANDOMCOFEE_TABLE_ID = Sequence('table_id_seq', start=10)
class RandomCoffee(Base):
    __tablename__ = "random_coffee"
    id = Column(Integer, RANDOMCOFEE_TABLE_ID, primary_key=True, server_default=RANDOMCOFEE_TABLE_ID.next_value())
    id_hobby = Column(Integer)
    tg_login = Column(String)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Base.metadata.create_all(engine)
