#!/usr/bin/env python3
""" This module create a ORM the User"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column


Base = declarative_base()


class User(Base):
    """This class Create the structure of the User"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250))
    hashed_password = Column(String(250))
    session_id = Column(String(250))
    reset_token = Column(String(250))
