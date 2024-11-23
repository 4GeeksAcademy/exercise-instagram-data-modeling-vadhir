import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True) 
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

# No borré nada: De aquí en adelante lo mío
class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")

class Comment(Base):
    __tablename__= 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(400), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="comments")
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post", back_populates="post_comments")

class Post(Base):
    __tablename__= 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="posts")
    post_comments = relationship("Comment", back_populates="comment")
    post_images = relationship("Post_image", back_populates="post")

class Image(Base):
    __tablename__= 'image'
    id = Column(Integer, primary_key=True)
    image_url = Column(String)
    images = relationship("Post_Image", back_populates="image")

class Post_Image(Base):
    __tablename__= 'post_image'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post_images = relationship("Post", back_populates="post_images")
    image_id = Column(Integer, ForeignKey('image.id'))
    images = relationship("Image", back_populates="images")


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
