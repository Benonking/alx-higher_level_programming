#!/usr/bin/python3
"""
Module 11-model_state_insert
insert state object to states table
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
    lousina = State(name='Lousiana')
    session.add(lousina)
    inst = session.query(State).filter_by(name='Lousiana').first()
    print(lousina.id)
    session.commit()
