#!/usr/bin/env python3
"""This module use asyncio for create funcion asyncronus"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """This funcion create and comprime the list for loop await"""
    return [i async for i in async_generator()]
