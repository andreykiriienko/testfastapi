from sqlalchemy import Column, Integer, String, ForeignKey, BOOLEAN
from sqlalchemy.orm import relationship
from config import Base, engine
import pymysql

pymysql.install_as_MySQLdb()


class Users(Base):
    __tablename__ = 'Users'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    email = Column(String(50), nullable=False, unique=True)
    connected_game = Column(BOOLEAN, nullable=False, default=False)


class Games(Base):
    __tablename__ = 'Games'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)


class Connections(Base):
    __tablename__ = 'Connections'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    game_id = Column(Integer, ForeignKey('Games.id'), nullable=False)
    user = relationship('Users')
    game = relationship('Games')


Base.metadata.create_all(engine)
