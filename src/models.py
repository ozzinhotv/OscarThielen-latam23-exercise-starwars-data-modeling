import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base): #Parent
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    mail = Column(String(250), unique= True, nullable=False)
    password = Column(Integer, nullable= False)

class Favorites(Base):
    __tablename__='favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id=Column(Integer, ForeignKey('character.id'))
    planet_id=Column(Integer, ForeignKey('planets.id'))
    user = relationship("User")
    character= relationship("Character") 
    planets= relationship("Planets")

class Character(Base):
    __tablename__='character'
    id=Column(Integer, primary_key=True)
    name=Column(String, unique=False, nullable=False)
    color_eyes= Column(String, unique=False,nullable=False)
    height= Column(String, unique= False, nullable=False)

class Planets(Base):
    __tablename__='planets'
    id=Column(Integer, primary_key=True)
    name=Column(String, unique=False, nullable=False)
    terrain= Column(String, unique=False,nullable=False)
    surface= Column(String, unique= False, nullable=False)


# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
