import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

PostSalved = Table("posts_salved", Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("posts_id", Integer, ForeignKey("posts.id")),
    Column("users_id", Integer, ForeignKey("users.id"))

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    phone = Column(Integer, nullable=False)
    birthdate = Column(DateTime, nullable=False)
    posts = relationship('Post', backref='users', lazy=True)
    stories = relationship('stories', backref='users', lazy=True)

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    date = Column(DateTime, nullable=False)
    hour = Column(DateTime, nullable=False)
    content = Column(String(250), nullable=False)
    multimedia = Column(String(250), nullable=False)
    label = Column(Integer, nullable=False)
    hastag = Column(DateTime, nullable=False)
    users_ID = Column(Integer, ForeignKey("users.id"))
    posts_salved = relationship('User', secondary=PosSalved, lazy="subquery", backref=backref('posts', lazy=True))


class Story(Base):
    __tablename__ = 'stories'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    date = Column(DateTime, nullable=False)
    hour = Column(DateTime, nullable=False)
    content = Column(String(250), nullable=False)
    multimedia = Column(String(250), nullable=False)
    label = Column(Integer, nullable=False)
    hastag = Column(DateTime, nullable=False)
    Users_ID = Column(Integer, ForeignKey("users.id"))




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

