#!/usr/bin/python3
"""
This Module contains a script that reads stdin line
by line and computes metrics
"""
from sys import stdin
from typing import Dict


def print_logs(size: int, res_dic: Dict[str, int]) -> None:
    """Print the log metrics"""
    print('File size: {}'.format(size))
    for k, v in sorted(res_dic.items()):
        if v != 0:
            """If the key is found in the file or stdin i.e its
            value increases, print it otherwise skip it"""
            print('{}: {}'.format(k, v))


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
            print_logs(total_size, status_codes_dict)

except KeyboardInterrupt:
    print_logs(total_size, status_codes_dict)
