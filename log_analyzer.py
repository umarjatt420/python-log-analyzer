import re
from collections import defaultdict

def analyze_logs(log_file):
    # Open the log file for reading
    with open(log_file, 'r') as file:
        log_counts = defaultdict(int)

        for line in file:
            line = line.strip()

            if not line:
                continue

            log_counts[line] += 1

    for log_message, count in log_counts.items():
        print(f"Log Message: '{log_message}', Count: {count}")

log_file = '/var/log/boot.log'
analyze_logs(log_file)