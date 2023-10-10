#!/usr/bin/env python3
""" Module Basic Auth"""
from .auth import Auth
from models.user import User
from models.base import Base
from typing import TypeVar
import base64


class BasicAuth(Auth):
    """This class inherit from Auth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """This method check an extract the authorization headers"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header.startswith("Basic "):
            value = authorization_header.replace("Basic ", "")
            return value
        else:
            return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                               str) -> str:
        """This method decode the header authorization"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decode_bytes = base64.b64decode(base64_authorization_header)
            return decode_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                     str) -> (str, str):
        """This method extract the credentias of the authorization heaers"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" in decoded_base64_authorization_header:
            dates = decoded_base64_authorization_header.split(":")
            return (dates[0], dates[1])
        else:
            return (None, None)

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd:
                                         str) -> TypeVar('User'):
        """ This method check credentials of user"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        users = User.all()
        for user in users:
            if user.email == user_email and user.is_valid_password(user_pwd):
                return user
            continue
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """This method check the current user"""
        return self.user_object_from_credentials(
            *self.extract_user_credentials(
                self.decode_base64_authorization_header(
                    self.extract_base64_authorization_header(request)
                )
            )
        )
