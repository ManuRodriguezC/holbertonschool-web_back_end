#!/usr/bin/env python3
""" Module Auth """
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User
import bcrypt


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ This method created and register User in db """
        try:
            USER: User = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)
        else:
            raise ValueError(f"User {email} already exists ")


def _hash_password(password: str) -> bytes:
    """ This method encrypt the password """
    byte = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(byte, salt)
