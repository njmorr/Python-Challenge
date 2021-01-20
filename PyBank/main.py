# print("Hello World")

import os

import csv

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # first FOR loop
    for column in csvreader:
        print(column[1])