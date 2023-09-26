#!/usr/bin/env python3
"""This module cron the time of the execute function"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    start: float = time.process_time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.process_time()

    total: float = start - end
    return total / n
