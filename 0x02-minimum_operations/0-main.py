#!/usr/bin/python3
"""
Main file for testing
"""
import time
minOperations = __import__('0-minoperations').minOperations

start = time.perf_counter()
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 1
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

elapsed = time.perf_counter() - start

print(f"Total time ==>{elapsed}")