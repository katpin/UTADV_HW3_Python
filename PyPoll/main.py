#Initiate Dependencies
import csv
import os

#Specify the file
file = os.path.join('Resources','election_data.csv')

#Open the file to be read and set the contents to list
with open(file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    election_data = list(csvreader)

#Total the votes by counting rows in election data list
votes = 0

votes = sum(1 for row in election_data)

#Find unique candidates and create a list
candidates = []

for row in election_data:
    if row[2] not in candidates:
        candidates.append(row[2])
cand_cnt = len(candidates)

#Count up for each candidate and create a list of vote counts
cand_votes = []

cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0

for row in election_data:
    if row[2] == candidates[0]:
        cand1 += 1
    if row[2] == candidates[1]:
        cand2 += 1
    if row[2] == candidates[2]:
        cand3 += 1
    if row[2] == candidates[3]:
        cand4 += 1

cand_votes.append(cand1)
cand_votes.append(cand2)
cand_votes.append(cand3)
cand_votes.append(cand4)

#Create a list taking the percent of votes
perc_votes = []

for i in range(0,cand_cnt):
    perc = round(cand_votes[i]/votes*100,3)
    perc_votes.append(perc)

#Zip together all the lists and find the max vote count and index
zipped = dict(zip(candidates,cand_votes))
winner = max(zipped, key=zipped.get)
listzip = list(zip(candidates,cand_votes,perc_votes))

#Print results
print(f"Election Results:")
print("-------------------------")
print(f"Total Votes: {votes}")
print("-------------------------")
for row in listzip:
    print(f"{row[0]}: {row[2]}% ({row[1]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#Write to new text file
f = open("PyPoll.txt", "w")

f.write(f"Election Results:\n")
f.write("-------------------------\n")
f.write(f"Total Votes: {votes}\n")
f.write("-------------------------\n")
for row in listzip:
    f.write(f"{row[0]}: {row[2]}% ({row[1]})\n")
f.write("-------------------------\n")
f.write(f"Winner: {winner}\n")
f.write("-------------------------\n")