#!/usr/bin/python3

"""
This Module contains a script that reads stdin line by line and computes metrics
"""
from sys import stdin
from typing import Dict

def print_log(total_size: int, status_codes: Dict[str, int]):
    """
    Prints log metrics
    """
    print(f"Total file size: {total_size}")
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print(f"{key}: {status_codes[key]}")

status_codes_dict = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
total_size = 0

try:
    for count, line in enumerate(stdin, 1):
        parts = line.split()
        if len(parts) == 9:
            status_code = parts[-2]
            try:
                file_size = int(parts[-1])
                total_size += file_size
                if status_code in status_codes_dict:
                    status_codes_dict[status_code] += 1
            except ValueError:
                pass

        if count % 10 == 0:
            print_log(total_size, status_codes_dict)

except KeyboardInterrupt:
    print_log(total_size, status_codes_dict)
