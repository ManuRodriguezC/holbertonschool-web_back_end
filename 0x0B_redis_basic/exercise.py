#!/usr/bin/env python3
""" Module to connect with redis """
import redis
import uuid


class Cache():
    """ This class create a redis connection"""
    _redis = redis.Redis()

    def store(self, data: str) -> str:
        """
        This method created the set with key and value.
        Parameters
        ----------
        data: String
            If the value of the key to save in redis db.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
