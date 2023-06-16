import os
import csv

election_data = os.path.join("Resources", "election_data.csv")


#variables
count = 0

#lists to store data
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

#open CSV
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #skip header
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csv_reader:
        #count = total number of votes
        count = count + 1 
        
         # candidate list
        candidatelist.append(row[2])

        # unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)

        # y = total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)

        # z = percent of total votes per candidate
        z = (y/count) * 100
        z_rounded = round(z, 3)
        vote_percent.append(z_rounded)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]


    #print in terminal
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(count))
    print("-------------------------")
    for i in range(len(unique_candidate)):
        print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
    print("-------------------------")
    print("Winner: " + winner)
    print("-------------------------")

    #text file
    with open('election_results.txt', 'w') as text:
        text.write("Election Results\n")
        text.write("---------------------------------------\n")
        text.write("Total Vote: " + str(count) + "\n")
        text.write("---------------------------------------\n")
        for i in range(len(set(unique_candidate))):
            text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
        text.write("---------------------------------------\n")
        text.write("The winner is: " + winner + "\n")
        text.write("---------------------------------------\n")