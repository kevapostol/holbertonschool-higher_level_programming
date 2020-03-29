#!/usr/bin/python3
"""
a python file that contains the class definition of a State and an instance
Base = declarative_base()

This is the configurational process starts by describing the database tables
we’ll be dealing with, and then by defining our own classes which will be
mapped to those tables
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
