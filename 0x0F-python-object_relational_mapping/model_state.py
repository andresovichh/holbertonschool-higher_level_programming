#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
Base = declarative_base()

class State(Base):
    """ definition of State class"""
    __tablename__ = 'states'
    id = Column("states.id", Integer, primary_key=True)
    name =  Column(String(128))
