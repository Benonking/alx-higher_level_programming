#!/usr/bin/python3
"""
Module 8-model_state_fetch_first
list first state in table states
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    inst = session.query(State).first()
    if inst is None:
        print("Nothing")
else:
    print(inst.id, inst.name, sep=": ")
