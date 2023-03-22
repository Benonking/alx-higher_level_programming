#!/usr/bin/python3
"""
Module 13-model_state_insert
Delete instance
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
    session.commit()
    for inst in session.query(State).filter(State.name.like('%a%')):
        session.delete(inst)
    session.commit()
