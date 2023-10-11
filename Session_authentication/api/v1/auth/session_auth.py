#!/usr/bin/env python3
"""Module Session Auth"""
from api.v1.auth.auth import Auth
from models.user import User
from uuid import uuid4
from typing import Union
import base64


class SessionAuth(Auth):
    """ Class Session auth """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
            This methos create a session auth
            Whit the user_id, create a key witj uuid4
            and save the values in the emply file
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        key: str = str(uuid4())
        self.user_id_by_session_id[key] = user_id

        return key

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
            This method check if session id exist
            if not exist or is other type return None
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        try:
            return self.user_id_by_session_id[session_id]
        except Exception:
            return None

    def current_user(self, request=None) -> Union[User, None]:
        """This method check is the ssesion is login
            if the session is on, take the id of teh user
            an get the user with the id fro come return user
        """
        if request is None:
            return None

        session = self.session_cookie(request)

        id = self.user_id_for_session_id(session)
        user = User.get(id)

        return user
