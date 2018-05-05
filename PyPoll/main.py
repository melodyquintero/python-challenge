# Import Modules for Reading raw data
import os
import csv

# Set path for file
csvpath = os.path.join('raw_data','election_data_1.csv')

# Lists to store data
ID = []
County = []
Candidate = []

# Open and read the CSV, excluding header
with open(csvpath, newline="") as csvfile:
    next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:

        # Add ID data to the list
        ID.append(row[0])

        # Add County data to the list
        County.append(row[1])

        # Add Candidate data to the list
        Candidate.append(row[2])


# Count total number of votes
Votes_count = len(ID)

# Import collections to group votes by different candidates
import collections
counter=collections.Counter(Candidate)

# With the results of collections, place candidate names and their votes to lists
candidate_name =list(counter.keys())
candidate_votes = list(counter.values())

# list candidate votes percentage to store data
candidate_percent = []

# calculate and formate votes percentage by candidates
for i in range(len(candidate_name)):
    candidate_i_percent='{0:.1%}'.format(float(candidate_votes[i])/Votes_count)
    # add candidates percentage to the list
    candidate_percent.append(candidate_i_percent)

# locate the index of highest votes and apply on candidate names to find the winner
Winner_index = candidate_votes.index(max(candidate_votes))
Winner = candidate_name[Winner_index]


# Print results on terminal
print("Election Results")
print("-"*30)

print("Total Votes: "+ str(Votes_count))
print("-"*30)

for j in range(len(candidate_name)):
    print(str(candidate_name[j])+": "+ str(candidate_percent[j])+ " ("+str(candidate_votes[j])+")")
print("-"*30)

print("Winner: "+str(Winner))
print("-"*30)

# Export Text File
with open("Election_Results.txt", "w+") as f:

    f.write("Election Results"+"\n")
    f.write("-"*30+"\n")

    f.write("Total Votes: "+ str(Votes_count)+"\n")
    f.write("-"*30+"\n")

    for j in range(len(candidate_name)):
        f.write(str(candidate_name[j])+": "+ str(candidate_percent[j])+ " ("+str(candidate_votes[j])+")"+"\n")
    f.write("-"*30+"\n")

    f.write("Winner: "+str(Winner)+"\n")
    f.write("-"*30+"\n")