#!/usr/bin/env python3
"""This module use asyncio for create funcion asyncronus"""
import asyncio
import random


async def async_generator():
    """
    This funcion generate a list of 10 values of the random number
    but with use yield, this reserved name is for create a return a value
    but waitng all values.
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
