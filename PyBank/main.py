# print("Hello World")

import os

import csv

import operator
# will be used below to find greatest increaes and decrease on a monthly basis
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
# Accessed 19 Jan 2021

csvpath = os.path.join('Resources','budget_data.csv')

# create empty lists
month = []
ledger = []
delta = []
deltaMod = []

deltaDict = dict()

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    sumOfMonth = 0
    total = 0
    greatestIncrease = 0
    greatestDecrease = 0
    sumOfDelta = 0

    # for loop for cycling through the data set
    for column in csvreader:
        month.append(column[0])
        ledger.append(int(column[1]))
 
    # count number of months in data set
        if ledger != 0:
            sumOfMonth = sumOfMonth + 1
  
    # sum up the total profits and losses in data set
    for PNL in ledger:
        total = total + PNL
        
    # create a version of the delta list that can be modified       
    for (i, value) in enumerate(ledger):
        previousPNL = ledger[i-1] if i > 0 else 0
        currentPNL = value
        deltaPNL = currentPNL - previousPNL
        deltaMod.append(int(deltaPNL))
    
    del deltaMod[0]
    # print(deltaMod)
    countOfChange = len(deltaMod)
    
    for monthlyDelta in deltaMod:
        sumOfDelta = sumOfDelta + monthlyDelta
    
   
    # find greatest increase month-to-month         
    for (i, value) in enumerate(ledger):
        previousPNL = ledger[i-1] if i > 0 else 0
        currentPNL = value
        deltaPNL = currentPNL - previousPNL
        delta.append(int(deltaPNL))
        # print(delta)
        # Comparing adjacent values in a list
        # https://www.quora.com/How-do-I-iterate-through-a-list-in-python-while-comparing-the-values-at-adjacent-indices
        # Accessed 19 January 2021
    # print(len(delta))  
    

    for m in month:
        for change in delta:
            deltaDict[m] = change
            delta.remove(change)
            break
        # Converting two lists into a dictionary
        # https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
        # Accessed 19 Jan 2021
    
    # print(delta)
    # print(deltaDict)

    greastestIncreaseMonth = (max(deltaDict.items(), key=operator.itemgetter(1))[0])
    greastestIncreasePNL = (max(deltaDict.items(), key=operator.itemgetter(1))[1])
    greastestDecreaseMonth = (min(deltaDict.items(), key=operator.itemgetter(1))[0])
    greastestDecreasePNL = (min(deltaDict.items(), key=operator.itemgetter(1))[1])
    # print(greastestDecreaseMonth)
    # print(greastestDecreasePNL)

Title = "Financial Analyis"
Line = "---------------------------------"
TotalMonths = f'Total Months: {sumOfMonth}'

TotalMonies = f'Total: ${total}'
averageChange = round(sumOfDelta/countOfChange,2)
# Rounding to 2 decimals
# https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
# accessed 19 Jan 2021    
CalculatedAverageChange = f'Average Change: {averageChange}'
GreatestIncrease = f'Greatest Increase in Profits: {greastestIncreaseMonth} (${greastestIncreasePNL})'
GreatestDecrease = f'Greatest Decrease in Profits: {greastestDecreaseMonth} (${greastestDecreasePNL})'

print(Title)
print (Line)
print(TotalMonths)
print(TotalMonies)
print(CalculatedAverageChange)
print(GreatestIncrease)
print(GreatestDecrease)

dataSummary = [Title, Line, TotalMonths, TotalMonies, CalculatedAverageChange, GreatestIncrease, GreatestDecrease]

# print(dataSummary)

#create and save the output file
output_file = os.path.join("analysis", "financial_analysis.csv")

with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile, delimiter='\t')
    writer.writerows(dataSummary)
# Use of delimiter parameter
# https://stackoverflow.com/questions/51100680/python-list-to-csv-file-with-each-item-in-new-line
# Accessed 19 Jan 2021
# delimeter = '\t'
# trial and error with random letters