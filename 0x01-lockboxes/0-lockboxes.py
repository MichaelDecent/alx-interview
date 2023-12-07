#!/usr/bin/python3
"""
This program determines if all the boxes (list of lists) can be opened.
"""

# def canUnlockAll(boxes):
#     """
#     Return True if all boxes can be opened, else return False
#     """
#     keys = boxes[0]
#     box_checked = False
#     position = 0
#     index = 0
#     while index < len(boxes) - 1:
#         if index+1 in keys:
#             keys.extend(boxes[index+1])
#             position += 1
#             index = position
#             box_checked = True
#         else:
#             index += 1
#             box_checked = False
#     return box_checked        
            


def canUnlockAll(boxes):
    if not boxes or len(boxes) == 0:
        return False

    box_status = {}

    for index, value in enumerate(boxes):
        box_status[index] = False

    box_status[0] = True

    for index, value in enumerate(boxes):
        for val in value:
            if box_status[index] == True:
                box_status[val] = True
            if val < index:
                for val in boxes[index]:
                    box_status[val] = True

    final_status = all(value for value in box_status.values())

    return final_status

    
                
