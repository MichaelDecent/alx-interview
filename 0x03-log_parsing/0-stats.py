#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order

"""
import sys
from ipaddress import ip_address
from datetime import datetime
from typing import Dict


def print_log(total_size: int, status_codes: Dict[str, int])-> None:
    """
    Prints log metrics
    """
    print(f"File size: {total_size}")
    for key, val in status_codes.items():
        if val != 0:
            print(f"{key}: {val}")



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
    for count, line in enumerate(sys.stdin, 1):
        format = line.split()
        status_code = format[7]
        file_size = int(format[8])
        total_size += file_size
        for key, val in status_codes_dict.items():
            if status_code == key:
                status_codes_dict[key] += 1

        if count % 10 == 0:
            print_log(total_size, status_codes_dict)
            

except KeyboardInterrupt:
    print_log(total_size, status_codes_dict)


# def check_format(format):
#     separators = [" ", "[", "]"
#     pattern = '|'.join(map(re.escape, separators)
#     format = re.split(pattern, line, 5)
#     print(format)
#     if ip_address(format[0]):
#         print(True)
#     else:
