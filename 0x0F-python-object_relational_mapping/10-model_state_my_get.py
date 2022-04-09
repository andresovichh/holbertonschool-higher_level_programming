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

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    item = session.query(State).filter(State.name.like(argv[4]))
    if item is None:
        print("Not found")
    else:
        print("{}".format(item.id))
