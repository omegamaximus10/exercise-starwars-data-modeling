import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person (Base):
    __tablename__ ='person'
    id = Column(Integer,primary_key= True)
    name = Column(String (250),primary_key= False)
    gender = Column(String (250),primary_key= False)
    height= Column(String (250),primary_key= False)
class Planet(Base):
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
    planet_id = Column(Integer, ForeignKey('planet.id'))
    Planet = relationship(Planet)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


render_er (Base,'diagram.png')