#!/usr/bin/env python3
""" Module Auth """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ This method encrypt the password """
    byte = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(byte, salt)
