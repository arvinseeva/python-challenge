# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    voter = 0
    khan = 0
    Correy = 0
    li = 0
    toole = 0
    for row in csvreader:
        voter += 1
        if row[2] == "Khan":
            khan += 1 

        if row[2] == "Correy":
                Correy += 1

        if row[2] == "Li":
                    li += 1

        if row[2] == "O'Tooley": 
                toole += 1

   # print(str(voter))
    
#Make candidate list
    candidates = []

    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
  
    
    print (str(candidates))

#Count votes

khancent = khan/voter * 100
correycent = Correy/voter * 100
licent = li/voter * 100
toolcent = toole/voter * 100

#Asses winner

winner = [
    khan,
    Correy,
    li,
    toole
]
win = max(winner)

if win == khan:
    winning = "Khan"
    
if win == Correy:
    winning = "Correy"

if win == li:
    winning = "Li"

if win == toole:
    winning = "O'Toole"



print ("Election Results")
print ("-----------------------------------------------")
print ("Total Votes :" + str(voter))
print ("-----------------------------------------------")
print ("Khan :" + str(khancent) + "% ("+ str(khan) + ")" )
print ("Correy "+ str(correycent) + "% (" + str(Correy) + ")")
print ("Li " + str(licent) + "% ("+ str(li) + ")")
print ("O'Tooley " + str(toolcent) + "% ("+ str(toole) + ")")
print ("-----------------------------------------------")
print ("Winner : " + winning)
print ("-----------------------------------------------")


# Specify the file to write to
output_path = os.path.join("..", "Analysis", "election.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as text_file:

 # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')


    print ("Election Results", file=text_file)
    print ("-----------------------------------------------", file=text_file)
    print ("Total Votes :" + str(voter))
    print ("-----------------------------------------------", file=text_file)
    print ("Khan :" + str(khancent) + "% ("+ str(khan) + ")" , file=text_file)
    print ("Correy "+ str(correycent) + "% (" + str(Correy) + ")", file=text_file)
    print ("Li " + str(licent) + "% ("+ str(li) + ")", file=text_file)
    print ("O'Tooley " + str(toolcent) + "% ("+ str(toole) + ")", file=text_file)
    print ("-----------------------------------------------", file=text_file)
    print ("Winner : " + winning, file=text_file)
    print ("-----------------------------------------------", file=text_file)