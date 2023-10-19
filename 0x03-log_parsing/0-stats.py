#!/usr/bin/python3
import re
import sys
from collections import defaultdict

# Regular expression to match the input format
log_pattern = re.compile(
           r'^([\d.]+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
)

# Initialize variables to store metrics
total_size = 0
status_code_counts = defaultdict(int)

line_count = 0

try:
    for line in sys.stdin:
        # Match the line with the regular expression
        match = log_pattern.match(line)
        if match:
            # Extract relevant information from the log entry
            # return all the captured groups as a tuple match.groups()
            ip_address, _, status_code, file_size = match.groups()

            # Update metrics
            total_size += int(file_size)
            status_code_counts[status_code] += 1

            line_count += 1

        # Check if processed 10 lines or more
        if line_count >= 10:
            # Print the statistics
            print(f'File size: {total_size}')
            for code in sorted(status_code_counts):
                print(f'{code}: {status_code_counts[code]}')

            # Reset counters
            line_count = 0
            total_size = 0
            status_code_counts = defaultdict(int)

except KeyboardInterrupt:
    # Handle a keyboard interruption (CTRL + C)
    for code in sorted(status_code_counts):
        print(f'{code}: {status_code_counts[code]}')

# Print the final statistics after reading all lines
print(f'Total file size: {total_size}')
for code in sorted(status_code_counts):
    print(f'{code}: {status_code_counts[code]}')
