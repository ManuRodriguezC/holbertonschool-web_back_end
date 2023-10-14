#!/usr/bin/env python3
""" This module create a ORM the User"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column


Base = declarative_base()

class User(Base):
    """"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    hashed_password = Column(String)
    session_id = Column(String)
    reset_token = Column(String)
