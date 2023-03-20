#!/usr/bin/python3
"""
Module model_state
State class defination with instance Base= declarative_bas()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

data = MetaData()
Base = declarative_base(metadata = data)


class State(Base):
    """
    Class definition of a state table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
