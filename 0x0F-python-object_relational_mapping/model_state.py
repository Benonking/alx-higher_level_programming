#!/usr/bin/python3
"""
Module model_state
State class defination with instance Base= declarative_bas()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.exit.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Class definition of a state table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
