#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User
from typing import Union


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add user in DB"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find a user in the database
        """
        USER: Union[User, None] = self._session.query(User) \
            .filter_by(**kwargs) \
            .first()

        if USER is None:
            raise NoResultFound

        return USER

    def update_user(self, id: int, **kwargs):
        """ Update user """
        USER: User = self.find_user_by(id=id)

        if 'id' in kwargs:
            raise ValueError("Cannot update 'id' of 'User'.")

        for attr, value in kwargs.items():
            if attr not in USER.__dict__.keys():
                raise ValueError(f"'User' object has no attribute '{attr}'")
            setattr(USER, attr, value)