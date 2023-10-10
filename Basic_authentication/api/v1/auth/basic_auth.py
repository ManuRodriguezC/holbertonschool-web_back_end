#!/usr/bin/env python3
""" Module Basic Auth"""
from .auth import Auth
from typing import TypeVar
import base64


class BasicAuth(Auth):
    """This class inherit from Auth"""
    pass

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
                                           base64_authorization_header: str) -> str:
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

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
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

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """"""