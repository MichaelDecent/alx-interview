#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesnt appear or is not an integer, dont print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""

#!/usr/bin/python3

import sys

def print_log(total_size, status_codes):
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
    for count, line in enumerate(sys.stdin, 1):
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
