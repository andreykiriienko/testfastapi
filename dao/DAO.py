from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config import Base, engine
import pymysql

pymysql.install_as_MySQLdb()


class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    age = Column(Integer)
    email = Column(String(50), nullable=False, unique=True)


class Games(Base):
    __tablename__ = 'Games'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    name = Column(String(100), nullable=False)
    user = relationship('Users')


Base.metadata.create_all(engine)
