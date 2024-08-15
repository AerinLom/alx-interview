#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""
import sys


def print_metrics(status_code_counts, total_file_size):
    """
    Method to print the metrics.
    """
    print("File size: {}".format(total_file_size))
    for status_code, count in sorted(status_code_counts.items()):
        if count != 0:
            print("{}: {}".format(status_code, count))


total_file_size = 0
line_count = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


try:
    for line in sys.stdin:
        reversed_line_parts = line.split()[::-1]

        if len(reversed_line_parts) > 2:
            line_count += 1

            total_file_size += int(reversed_line_parts[0])
            status_code = reversed_line_parts[1]

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            if line_count == 10:
                print_metrics(status_code_counts, total_file_size)
                line_count = 0

finally:
    print_metrics(status_code_counts, total_file_size)
