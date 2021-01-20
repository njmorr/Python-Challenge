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

    # Sum all the votes (keys) in dictionary
    totalVotes = 0
    
    for votes in countedVotes.values():
        totalVotes = totalVotes + int(votes)
    # print(totalVotes)
    # proper syntax
    # https://realpython.com/iterate-through-dictionary-python/
    # Accessed 20 January 2021

    # candidate1 = "Khan"
    # candidate2 = "Correy"
    # candidate3 = "Li"
    # candidate4 = "O'Tooley"


    candidate1Votes = countedVotes["Khan"]
    
    print(candidate1Votes)