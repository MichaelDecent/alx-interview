#!/usr/bin/python3
"""
This program determines if all the boxes (list of lists) can be opened.
"""


def canUnlockAll(boxes):
    """
    Return True if all boxes can be opened, else return False
    """
    if not boxes or len(boxes) == 0:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    keys = [0]

    while keys:
        current_box = keys.pop(0)

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                keys.append(key)

    return all(visited)
