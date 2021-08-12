import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class person (base):
    __tablename__ ='person'
    id = column(Integer,primary_key= True)
    name = column(String (250),primary_key= False)
    gender = column(String (250),primary_key= False)
    height= column(String (250),primary_key= False)

class Planeta(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    gravity = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)
    climate = Column(Integer, nullable=False)
    
 class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(Integer, nullable=False)
    
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    planeta_id = Column(Integer, ForeignKey('planeta.id'))
    Planeta = relationship(Planeta)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)








#class Person(Base):
#
#
#   __tablename__ = 'person'
# Here we define columns for the table person
# Notice that each column is also a normal Python instance attribute.
#   id = Column(Integer, primary_key=True)
#   name = Column(String(250), nullable=False)

#class Address(Base):
#   __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    street_name = Column(String(250))
#   street_number = Column(String(250))
#    post_code = Column(String(250), nullable=False)
#   person_id = Column(Integer, ForeignKey('person.id'))
#    person = relationship(Person)

#    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')