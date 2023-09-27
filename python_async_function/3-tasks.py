#!/usr/bin/env python3
"""This module return the tipe of the object"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function execute the function and return of the type
    """
    wait = asyncio.Task(wait_random(max_delay))
    return wait
