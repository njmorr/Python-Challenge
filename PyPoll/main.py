#print("Hello World")

import os

import csv

csvpath = os.path.join('Resources','election_data.csv')


votes = []
countedVotes = dict()

title = "Election Results"
print(title)
line = "-----------------------------"
print(line)


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

    # print(countedVotes)
    # Using dictionaries as a counter
    # Severance, C., Andrion, A., Hauser, E., & Blumenberg, S. 
    # (2016). Python for Everybody: Exploring Data in Python 3. Self-Published.
    # Page 109

    # Sum all the votes (keys) in dictionary
    totalVotes = 0
    mostVotes = 0
    for votes in countedVotes.values():
        totalVotes = totalVotes + int(votes)
    
    totaledVotes = f'Total Votes: {totalVotes}'
    print(totaledVotes)
    print(line)
    
    # proper syntax
    # https://realpython.com/iterate-through-dictionary-python/
    # Accessed 20 January 2021
    
    
    # print(type(countedVotes))
    for key in countedVotes:
        print(f'{key}: {countedVotes[key]*100/totalVotes: .3f}% ({countedVotes[key]})')


    print(line)

    # finding a winner
    for candidate in countedVotes:
        if countedVotes[candidate] > mostVotes:
            mostVotes = countedVotes[candidate]
            winner = candidate
    
    winnerWinner = f'Winner: {winner}'
    print(winnerWinner)
    print(line)
    # traversing dictionaries and storing keys and values
    # Severance, C., Andrion, A., Hauser, E., & Blumenberg, S. 
    # (2016). Python for Everybody: Exploring Data in Python 3. Self-Published.
    # Page 112

# write to .csv
output_path = os.path.join("analysis", "election_analysis.csv")

with open(output_path, 'w') as datafile:
    datafile.write(title + '\n')
    datafile.write(line + '\n')
    datafile.write(totaledVotes + '\n')
    datafile.write(line + '\n')
    datafile.write(title + '\n')
    datafile.write(title + '\n')
    datafile.write(title + '\n')
    datafile.write(title + '\n')
    datafile.write(line + '\n')
    datafile.write(winnerWinner + '\n')
    datafile.write(line + '\n')
    
    # candidate1 = "Khan"
    # candidate2 = "Correy"
    # candidate3 = "Li"
    # candidate4 = "O'Tooley"


    # candidate1Votes = countedVotes["Khan"]
    # candidate2Votes = countedVotes["Correy"]
    # candidate3Votes = countedVotes["Li"]
    # candidate4Votes = countedVotes["O'Tooley"]

    # candidate1Percent = format(candidate1Votes/totalVotes*100, '.3f')
    # candidate2Percent = format(candidate2Votes/totalVotes*100, '.3f')
    # candidate3Percent = format(candidate3Votes/totalVotes*100, '.3f')
    # candidate4Percent = format(candidate4Votes/totalVotes*100, '.3f')
    # # formatting the decimal
    # # https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
    # # Accessed 20 January 2021

    # title = "Election Results"
    # line = "-----------------------------"
    # allVotes = f'Total Votes: {totalVotes}'

    # candidate1Results = f'{candidate1}: {candidate1Percent}% ({candidate1Votes})'
    # candidate2Results = f'{candidate2}: {candidate2Percent}% ({candidate2Votes})'
    # candidate3Results = f'{candidate3}: {candidate3Percent}% ({candidate3Votes})'
    # candidate4Results = f'{candidate4}: {candidate4Percent}% ({candidate4Votes})'
    
    # WinnerWinner = f'Winner: {winner}'

    # # Printing results:    
    # print(title)
    # print (line)
    # print(allVotes)
    # print (line)
    # print(candidate1Results)
    # print(candidate2Results)
    # print(candidate3Results)
    # print(candidate4Results)
    # print (line)
    # print(WinnerWinner)
    # print (line) 

# write to .csv
# output_path = os.path.join("analysis", "election_analysis.csv")

# with open(output_path, 'w', newline='') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter = ',')
#     csvwriter.writerows([title, line, allVotes, line, 
#     candidate1Results, candidate2Results, candidate3Results, 
#     candidate4Results, line, WinnerWinner, line])