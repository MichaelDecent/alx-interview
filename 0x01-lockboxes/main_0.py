#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [], [0, 4, 1], [3], [], [4, 1], []]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3, 8], [], [4, 1], [5, 6, 7]]
print(canUnlockAll(boxes))

boxes2 = [[1, 5], [3, 0, 1], [2, 6], [0]]
print(canUnlockAll(boxes2))

