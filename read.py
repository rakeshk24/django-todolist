# names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for line in sorted(names):
#     print(line)

import csv
import sys

try:
    with open("names.csv", 'r') as file:
        csv_reader = csv.reader(file)
        for row_num, row in enumerate(csv_reader, 1):
            if len(row) != 2:
                print(f"Warning: Row {row_num} has {len(row)} columns, expected 2", file=sys.stderr)
                continue

            name, age_str = row
            try:
                age = int(age_str)
                print(f"{name}'s age is {age}")
            except ValueError:
                print(f"Warning: Invalid age '{age_str}' for {name} on row {row_num}", file=sys.stderr)
except FileNotFoundError:
    print("Error: names.csv file not found", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error reading file: {e}", file=sys.stderr)
    sys.exit(1)
