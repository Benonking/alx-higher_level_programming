#!/usr/bin/python3
"""
Module 14-model_city_fetch_by_state
Fetech all cities from the database
"""
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy import (create_engine)
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for inst in session.query((State.name, City.id, City.name)
                              .filter(State.id == City.state_id)):
        print(inst[0] + ": " + "(" + str(inst[1]) + ") " + inst[2])
