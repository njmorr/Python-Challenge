# print("Hello World")

import os

import csv

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    sumOfMonth = 0
    total = 0
    
    # first FOR loop
    for column in csvreader:
        #print(column[1])
        ledger = [int(column[1])]      
        #print(type(ledger))

        if ledger != 0:
            sumOfMonth = sumOfMonth + 1
  
        for PNL in ledger:
            total = total + PNL
       

    print(f'Total Months: {sumOfMonth}')
    print(f'Total: ${total}')
