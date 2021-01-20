#print("Hello World")

import os

import csv

csvpath = os.path.join('Resources','election_data.csv')

votes = []
countedVotes = dict()

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    # print(csv_header)

    # turn the votes into a list
    for column in csvreader:
        votes.append(column[2])

    # put list into counted dictionary
    for vote in votes:
        if vote not in countedVotes:
            countedVotes[vote] = 1
        else:
            countedVotes[vote] = countedVotes[vote] + 1

    print(countedVotes)
    # Using dictionaries as a counter
    # Severance, C., Andrion, A., Hauser, E., & Blumenberg, S. 
    # (2016). Python for Everybody: Exploring Data in Python 3. Self-Published.
    # Page 109
    