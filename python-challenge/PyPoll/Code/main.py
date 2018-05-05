# Written by: Daniel Morales
# The following script is used to analyze election data and provide the outcome of the election.

# Import needed modules
import os
import csv

#Establish path to csv file of interest
file = input("What file would you like to analyze?\n\tPotential Options:\n\telection_data_1.csv\n\telection_data_2.csv\n------------------------\n")
csvpath = os.path.join('..','raw_data', file)

#read csv file
with open(csvpath, newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Calculate Total # of Votes Cast
    votercount = 0                                                      #voter counter
    voter_votes = list()                                                #est. list of voter votes
    for row in csvreader:
        votercount += 1                                                 # increment voter counter
        voter_votes.append(row[2])                                      # place voter's votes into list
    
    #A Complete List of Candidates who received votes
    candidates = []
    
    #Create list of unique names from data
    for names in voter_votes:
        if names not in candidates:
            candidates.append(names)
   
    #Clean data by dropping header
    candidates.remove("Candidate")
    
    #Tally Votes
    candidate_tallies = list()
    candidate_percentages = list()
    for name in candidates:
        count = 0                                                       #reset vote counter for every candidate
        for vote in voter_votes:
            if vote == name:                                            #if the vote has the name of the candidate, increment vote count
                count += 1
        candidate_tallies.append(count)                                 #append candidate tallies to list
        candidate_percentages.append(round(count/votercount*100,2))     #append cadidate percentage of total vote to list
    
    #Determine winner of election by finding the candidate with the greatest percentage of votes
    winner = candidates[candidate_percentages.index(max(candidate_percentages))]

# Set output path for output text file
output_path = os.path.join("..", "output", "results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
file = open(output_path, "w")

#write results into text file
file.write("Election Results\n------------------------\nTotal Votes: "+str(votercount)+"\n------------------------\n")
for name, percent, votes in zip(candidates,candidate_percentages,candidate_tallies):
    file.write(name + ": " + str(percent) + "%\t" + "("+ str(votes) + ")\n")
file.write("------------------------\nWinner: "+ winner + "\n")

#close file
file.close()








