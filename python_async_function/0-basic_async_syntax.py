#!/usr/bin/env python3
"""This module create a function that wait delay time"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function is async and give one param
    max_delay is a time delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
