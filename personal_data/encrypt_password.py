#!/usr/bin/env python3
"""Bycript password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    This method encrypt the password,
    this never save in database in encode.
    """
    pw_bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(pw_bytes, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    This function check if the password is same that
    encrypt password
    """
    pw = password.encode("utf-8")
    if bcrypt.checkpw(pw, hashed_password):
        return True
    else:
        return False
