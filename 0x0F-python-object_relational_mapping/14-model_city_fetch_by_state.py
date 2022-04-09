#!/usr/bin/python3

"""
Module thet lists all State objects from the
database hbtn_0e_6_usa
"""

from sys import argv
import sqlalchemy
from requests import Session
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine, null)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for item in session.query(State, City).\
            filter(State.id == City.state_id):
        print("{}: ({}) {}".format(item.State.name,
                                   item.City.id, item.City.name))
