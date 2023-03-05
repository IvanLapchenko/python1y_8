from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from flask_login import UserMixin

database = (create_engine('sqlite:///app.db', connect_args={"check_same_thread": False}))
Session = sessionmaker(bind=database)
session = Session()
Base = declarative_base()


class Student(Base, UserMixin):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)  # primary_key = False DEFAULT
    age = Column(Integer)
    address = Column(String)
    username = Column(String(60), unique=True)
    password = Column(String)
    group = Column(Integer, ForeignKey("group.id"))

    def __init__(self, name, age, address, username, password, group):
        super().__init__()
        self.name = name
        self.age = age
        self.address = address
        self.username = username
        self.password = password
        self.group = group


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)  # primary_key = False DEFAULT

    def __init__(self, name):
        super().__init__()
        self.name = name


Base.metadata.create_all(database)
