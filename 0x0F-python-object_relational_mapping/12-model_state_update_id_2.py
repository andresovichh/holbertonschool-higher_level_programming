#!/usr/bin/python3

"""
Module thet lists all State objects from the
database hbtn_0e_6_usa
"""

from sys import argv
import sqlalchemy
from requests import Session
from model_state import Base, State
from sqlalchemy import (create_engine, null)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    new = session.query(State).filter(State.id == 4).first()
    new.name = 'New Mexico'
    session.commit()
