#print("Hello World")

import os

import csv

votes = []
countedVotes = dict()

title = "Election Results"
print(title)
line = "-----------------------------"
print(line)

# write to .csv
output_path = os.path.join("analysis", "election_analysis.csv")

with open(output_path, 'w') as datafile:
    datafile.write(title + '\n')
    datafile.write(line + '\n')

csvpath = os.path.join('Resources','election_data.csv')

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

    # Using dictionaries as a counter
    # Severance, C., Andrion, A., Hauser, E., & Blumenberg, S. 
    # (2016). Python for Everybody: Exploring Data in Python 3. Self-Published.
    # Page 109

    # Sum all the votes (keys) in dictionary
    totalVotes = 0
    mostVotes = 0
    for votes in countedVotes.values():
        totalVotes = totalVotes + int(votes)
        # proper syntax
        # https://realpython.com/iterate-through-dictionary-python/
        # Accessed 20 January 2021
    
    totaledVotes = f'Total Votes: {totalVotes}'
    print(totaledVotes)
    print(line)
    with open(output_path, 'a') as datafile:
        datafile.write(totaledVotes + '\n')
        datafile.write(line + '\n')
    # Appending a file, and not writing over previous work
    # https://stackoverflow.com/questions/13203868/how-to-write-to-csv-and-not-overwrite-past-text
    # Accessed 22 Jan 2021    
    
    for key in countedVotes:
        candidateStats = f'{key}: {countedVotes[key]*100/totalVotes: .3f}% ({countedVotes[key]})'
        print(candidateStats)
        # formatting the decimals
        # https://thepythonguru.com/python-string-formatting/#:~:text=2f%20are%20called%20as%20format,the%20tuple%20i.e%2012%20and%20%25.
        # Accessed 22 Jan 2021
        with open(output_path, 'a') as datafile:
            datafile.write(candidateStats + '\n')

    # finding a winner
    for candidate in countedVotes:
        if countedVotes[candidate] > mostVotes:
            mostVotes = countedVotes[candidate]
            winner = candidate
    # traversing dictionaries and storing keys and values
    # Severance, C., Andrion, A., Hauser, E., & Blumenberg, S. 
    # (2016). Python for Everybody: Exploring Data in Python 3. Self-Published.
    # Page 112  

    winnerWinner = f'Winner: {winner}'
    print(line)
    print(winnerWinner)
    print(line)
    with open(output_path, 'a') as datafile:
        datafile.write(line + '\n')
        datafile.write(winnerWinner + '\n')
        datafile.write(line + '\n')
