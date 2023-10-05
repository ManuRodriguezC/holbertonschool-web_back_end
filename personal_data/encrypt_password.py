#!/usr/bin/env python3
"""Bycript password"""
import bcrypt


def hash_password(password: str):
    """
    This method encrypt the password,
    this never save in database in encode.
    """
    pw_bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(pw_bytes, bcrypt.gensalt())
    return hashed
