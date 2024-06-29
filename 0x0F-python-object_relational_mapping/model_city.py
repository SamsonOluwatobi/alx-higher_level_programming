#!/usr/bin/python3
"""This module defines a City model class with SQLAlchemy.

It represents a city in the database. The class has three attributes:

- id: an integer primary key that automatically increments
- name: a string representing the name of the city
- state_id: an integer foreign key to the State model

"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State

Base = declarative_base()


class City(Base):
    """City model."""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
