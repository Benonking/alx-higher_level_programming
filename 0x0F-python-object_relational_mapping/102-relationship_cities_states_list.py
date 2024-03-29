#!/usr/bin/python3
"""
Module 102-relationship_states_cities_list
list all State objects, and corespondoing City objects in db
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).join(City).order_by(City.id).all()

    for state in query:
        for cty in state.cities:
            print("{}: {} -> {}".format(cty.id, cty.name, state.name))
    session.close()
