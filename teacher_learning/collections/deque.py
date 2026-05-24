#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
deque

Phase: PHASE 1 — Core Python Repair
Also connects to PHASE 5 — Applied Python, especially trading systems, queues, rolling windows,
 and recent logs.

deque is pronounced:

deck

It stands for:

double-ended queue

Meaning:

A container where you can efficiently add/remove items from both the left side and right side.
"""

'''
append()       # add to right
appendleft()   # add to left
pop()          # remove from right
popleft()      # remove from left

maxlen

extend() -> Adds many items to the right.
extendleft() -> Adds many items to the left, but order becomes reversed.
clear() -> Removes everything.
count() -> Counts how many times a value appears.
remove() -> Removes the first matching value

'''

# from collections import deque

# tasks = deque()

# tasks.append("A")
# tasks.append("B")
# tasks.append("C")

# print(tasks)

# print(tasks.popleft())
# print(tasks)

# tasks.append("D")
# print(tasks)

# print(tasks.pop())
# print(tasks)

###############################################################################
'''
use of maxlen

'''
# Real trading example: last 5 prices

# from collections import deque

# last_5_prices = deque(maxlen=5)

# prices = [22450, 22455, 22460, 22440, 22470, 22480, 22490]

# for price in prices:
#     last_5_prices.append(price)
#     print(last_5_prices)




'''
deque feature:

rotate()

rotate() shifts items around.

'''

from collections import deque

d = deque([1, 2, 3, 4, 5])

d.rotate(1) # rotate(1) moves items one step to the right.

print(d)



d.rotate(-1) # rotate(-1) moves items one step to the left.

print(d) 



















