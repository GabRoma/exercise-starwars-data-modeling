import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# User
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
class CharactersDetails(Base):
    __tablename__ = 'charactersdetails'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters= relationship(Characters)
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    hairColor = Column(String(250), nullable=False)
    eyeColor = Column(String(250), nullable=False)
    skinColor = Column(String(250), nullable=False)
    birthYear = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    homeworld = Column(String(250), ForeignKey('planets.url'), nullable=False)
    planets = relationship(Planets)
    films = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    vehicles = Column(String(250), ForeignKey('vehicles.url') ,nullable=False)
    vehicles = relationship(Vehicles)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
class PlanetsDetails(Base):
    __tablename__ = 'planetsdetails'
    id = Column(Integer, primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    climate = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    orbitalPeriod = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    residents = Column(String(250), ForeignKey('characters.url'), nullable=False)
    characters = relationship(Characters)
    rotationPeriod = Column(String(250), nullable=False)
    surfaceWater = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
class VehiclesDetails(Base):
    __tablename__ = 'vehiclesdetails'
    id = Column(Integer, primary_key=True)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)
    cargoCapacity = Column(String(250), nullable=False)
    consumables = Column(String(250), nullable=False)
    costinCredits = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    manufactured = Column(String(250), nullable=False)
    maxAtmSpeed = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    pilots = Column(String(250), ForeignKey('characters.url'), nullable=False)
    characters = relationship(Characters)
    films = Column(String(250), nullable=False)
    vehicleClass = Column(String(250), nullable=False)
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)

    # def to_dict(self):
    #     return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')