#!/usr/bin/env python3
"""
This file retuns n numbers of times wait_random
"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This function create a list of the wait random numbers"""
    lists = []
    count = 0
    print("test")
    while count < n:
        number = await task_wait_random(max_delay)
        print(number)
        lists.append(number)
        count += 1
        lists.sort()
    return lists
