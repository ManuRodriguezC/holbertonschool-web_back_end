#!/usr/bin/env python3
"""
This file retuns n numbers of times wait_random
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """This function create a list of the wait random numbers"""
    lists = []
    count = 0
    while count < n:
        number = await wait_random(max_delay)
        lists.append(number)
        count += 1
    return lists
