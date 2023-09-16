#!/usr/bin/python3
"""Defines the City class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Represents a city in the database"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
