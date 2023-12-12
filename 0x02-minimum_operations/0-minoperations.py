#!/usr/bin/env python3
"""
"""

def minOperations(n):
    """
    a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file
    """
    if n <= 1:
        return 0

    no_ops = 0
    no_char_copied = 1
    while no_char_copied <= n:
        no_char_copied = copy_paste(no_char_copied)
        no_ops += 2
        if n == no_char_copied:
            return no_ops
        if determine_ops(paste, no_char_copied, n):
            no_char_copied += paste(no_char_copied)
            no_ops += 1
            return no_ops
        elif determine_ops(copy_paste, no_char_copied, n):
            no_char_copied = copy_paste(no_char_copied)
            no_ops += 2
            return no_ops
        
        no_char_copied += paste(no_char_copied)
        no_ops += 1
        if n == no_char_copied:
            return no_ops
        if determine_ops(paste, no_char_copied, n):
            no_char_copied += paste(no_char_copied)
            no_ops += 1
            return no_ops
        elif determine_ops(copy_paste, no_char_copied, n):
            no_char_copied = copy_paste(no_char_copied)
            no_ops += 2
            return no_ops
            
                       


def copy_paste(no_char):
    """
    returns times two of number of caharacter passed as agrument
    """
    return no_char * 2

def paste(no_char):
    """
    returns the extact number of character passed an argument
    """
    return no_char / 2

def determine_ops(operation, no_char, expected_char):
    """
    """
    no_char = operation(no_char)
    return True if no_char == expected_char else False

# print(determine_ops(copy_paste, 2, 4))
# def checker(n, n2):
#     """
#     """
#     return True if n == n2 else False