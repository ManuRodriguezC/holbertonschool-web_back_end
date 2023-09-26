#!/usr/bin/env python3
"""This module cron the time of the execute function"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    start_time = time.process_time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.process_time()
    total_time = end_time - start_time
    average_time = total_time / n
    return average_time
