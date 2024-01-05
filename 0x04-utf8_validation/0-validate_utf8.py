#!/usr/bin/python3
"""
This Module contains a method that determines if
a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    Return: True if data is a valid UTF-8 encoding, else return False
    """
    # Variable to track the number of bytes in the current UTF-8 character
    bytes_to_follow = 0

    for byte in data:
        # Checking the 8 least significant bits to determine the UTF-8 encoding
        if bytes_to_follow == 0:
            if (byte >> 3) == 0b11110:  # 4-byte character
                bytes_to_follow = 3
            elif (byte >> 4) == 0b1110:  # 3-byte character
                bytes_to_follow = 2
            elif (byte >> 5) == 0b110:  # 2-byte character
                bytes_to_follow = 1
            elif (byte >> 7) == 0b0:  # 1-byte character
                continue  # No need to check further for a single-byte characte
            else:
                return False  # Invalid UTF-8 sequence
        else:
            if (byte >> 6) != 0b10:
                return False  # Invalid UTF-8 sequence
            bytes_to_follow -= 1

    return bytes_to_follow == 0  # All multi-byte sequences wereclosed properly
