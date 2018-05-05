# The following script is used to analyze election data and provide the outcome of the election.
import os
import csv

directory = os.fsencode('../raw_data')
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    csvpath = os.path.join('..','raw_data', filename)
    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        # Calculate Total # of Votes Cast
        votercount = 0                                                     
        voter_votes = list()                                              
        for row in csvreader:
            votercount += 1                                                
            voter_votes.append(row[2])                                      
        candidates = []
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
                if vote == name:                                            
                    count += 1                                              #tally votes
            candidate_tallies.append(count)                                 
            candidate_percentages.append(round(count/votercount*100,2))    
        winner = candidates[candidate_percentages.index(max(candidate_percentages))]

    output_path = os.path.join("..", "output", filename + "_results.txt")
    file = open(output_path, "w")
    file.write("Election Results from " + filename + "\n------------------------\nTotal Votes: "+str(votercount)+"\n------------------------\n")
    for name, percent, votes in zip(candidates,candidate_percentages,candidate_tallies):
        file.write(name + ": " + str(percent) + "%\t" + "("+ str(votes) + ")\n")
    file.write("------------------------\nWinner: "+ winner + "\n")
    file.close()








