#!/usr/bin/env python3
'''Tasks'''


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def wait_task_random(max_delay: int) -> asyncio.Task:
    '''Waits for a random number of seconds'''
    return asyncio.create_task(wait_random(max_delay))