#!/usr/bin/python3
"""script that lists all State objects"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import Base, City
from model_state import State
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = {}
    for st in session.query(State).order_by(State.id).all():
        state[st.id] = st.name
    for city in session.query(City).order_by(City.id).all():
        print("{}: ({}) {}"
              .format(state[city.state_id], city.id, city.name))
    session.close()
