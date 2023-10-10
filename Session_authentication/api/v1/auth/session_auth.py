#!/usr/bin/env python3
"""Module Session Auth"""
from api.v1.auth.auth import Auth
import base64
from uuid import uuid4


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
