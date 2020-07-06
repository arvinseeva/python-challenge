# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    month = 0
    total = 0
    maximum = 0
    minimum = 0
    for row in csvreader:
        month += 1
        total += int(row[1])
        average = total/month

    for row in csvreader:

        if maximum > int(row[1]):
            maximum = int(row[1])
    
    for row in csvreader:
        if minimum < int(row[1]):
            minimum = int(row[1])
 

    print (maximum)
    print (minimum)

    #Print output
    print("Financial Analysis")
    print("------------------------------")
    print("Month " + str(month) )
    print("Total " + str(total) )
    print("Average " + str(average))


# Specify the file to write to
output_path = os.path.join("..", "Analysis", "Financial_Analysis.txt")
with open(output_path, 'w', newline='') as text_file:

# Open the file using "write" mode. Specify the variable to hold the contents

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    #csvwriter.writerow(["Financial Analysis"])
    print("Financial Analysis", file=text_file)
    #csvwriter.writerow(["------------------------------"])
    print('-----------------------------', file=text_file)
    #csvwriter.writerow(["Month " + str(month)])
    print("Month " + str(month), file=text_file)
    #csvwriter.writerow(["Total " + str(total)])
    print("Total " + str(total), file=text_file)
    #csvwriter.writerow(["Average " + str(average)])
    print("Average " + str(average), file=text_file)

csvfile.close()


