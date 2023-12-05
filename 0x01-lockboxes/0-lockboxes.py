#!/usr/bin/python3
"""
This program determines if all the boxes (list of lists) can be opened.
"""

def canUnlockAll(boxes):
    """
    Return True if all boxes can be opened, else return False
    """
    keys = boxes[0]
    box_checked = False
    position = 0
    index = 0
    while index < len(boxes) - 1:
        if index+1 in keys:
            keys.extend(boxes[index+1])
            position += 1
            index = position
            box_checked = True
        else:
            index += 1
            box_checked = False
    return box_checked        
            