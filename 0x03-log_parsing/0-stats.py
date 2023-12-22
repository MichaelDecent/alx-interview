#!/usr/bin/python3
"""
This Module contains a script that reads stdin line
by line and computes metrics
"""
from sys import stdin
from typing import Dict


def print_logs(size: int, res_dic: Dict[str, int]) -> None:
    """Print the log metrics"""
    print("File size: {}".format(size))
    for k, v in sorted(res_dic.items()):
        if v != 0:
            """If the key is found in the file or stdin i.e its
            value increases, print it otherwise skip it"""
            print("{}: {}".format(k, v))


responseDic = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

line_counter = 0
size = 0

try:
    for line in stdin:
        """Only print when 10 lines has been read"""
        if line_counter != 0 and line_counter % 10 == 0:
            print_logs(size, responseDic)

        line_counter += 1
        """Convert each line to a list for easy parsing using space"""
        lineArr = line.split()
        try:
            size += int(lineArr[-1])
        except Exception:
            pass

        try:
            key = lineArr[-2]
            if key in responseDic:
                responseDic[key] += 1
        except Exception:
            pass
    print_logs(size, responseDic)

except KeyboardInterrupt:
    """Print when ctrl-c is pressed"""
    print_logs(size, responseDic)
    raise
