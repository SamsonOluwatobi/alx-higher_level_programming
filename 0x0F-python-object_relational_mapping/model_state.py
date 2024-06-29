#!/usr/bin/python3
"""Defines a State model with SQLAlchemy, used to represent a state in the
database.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state in the database."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
