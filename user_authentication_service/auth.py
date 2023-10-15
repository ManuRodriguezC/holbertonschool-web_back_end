#!/usr/bin/env python3
""" Module Auth """
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User
import bcrypt
import uuid

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

    def valid_login(self, email: str, password: str) -> bool:
        """Valid teh user session"""
        try:
            USER: User = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            return bcrypt.checkpw(password.encode(), USER.hashed_password)

    def create_session(self, email: str) -> str:
        """ Create ID sesion when the user start session"""
        try:
            USER: User = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            ID_SESSION: str = _generete_uuid()
            self._db.update_user(USER.id, session_id=ID_SESSION)
            return ID_SESSION


def _generete_uuid() -> str:
    """Generate id unique """
    return str(uuid.uuid4())


def _hash_password(password: str) -> bytes:
    """ This method encrypt the password """
    byte = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(byte, salt)
