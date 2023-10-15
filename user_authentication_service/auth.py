#!/usr/bin/env python3
""" Module Auth """
from sqlalchemy.orm.exc import NoResultFound
from typing import Optional
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
            ID_SESSION: str = _generate_uuid()
            self._db.update_user(USER.id, session_id=ID_SESSION)
            return ID_SESSION

    def get_user_from_session_id(self, session_id: int) -> Optional[User]:
        """ This methods take the user with the ID """
        try:
            USER: User = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return USER

    def destroy_session(self, user_id: int) -> None:
        """ Destroy session of the user ID"""
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """ This method set and update the resent token """
        try:
            USER: User = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError(f"User with email={email} doesn't exist.")
        RESENT_TOKEN: str = _generate_uuid()
        self._db.update_user(USER.id, resent_token=RESENT_TOKEN)
        return RESENT_TOKEN

    def update_password(self, reset_token: str, password: str) -> None:
        """ Update password """
        try:
            USER: User = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError(f"Invalid password reset token: {reset_token}")

        PW: str = _hash_password(password)

        try:
            self._db.update_user(USER.id, reset_token=None, hashed_password=PW)
        except (NoResultFound, ValueError, Exception):
            raise


def _generate_uuid() -> str:
    """Generate id unique """
    return str(uuid.uuid4())


def _hash_password(password: str) -> bytes:
    """ This method encrypt the password """
    byte = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(byte, salt)
