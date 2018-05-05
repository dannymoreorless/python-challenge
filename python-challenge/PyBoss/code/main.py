# Written by: Daniel Morales
# Script used to convert employee data 

# Import needed modules
import os
import csv
#Establish path to csv file of interest
file = input("What file would you like to analyze?\n\tPotential Options:\n\temployee_data1.csv\n\temployee_data2.csv\n------------------------\n")

#establish path to desired csv file
csvpath = os.path.join('..','raw_data', file)

#declare US state abbreviations dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#declare empty lists for reformatted data
emp_id = list()
first_name = list()
last_name = list()
dob = list()
ssn = list()
state = list()
i = 0                                               # serves as a flag to skip labels on csv

#Read CSV
with open(csvpath, newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        if i == 0:                                  # skip over labels from csv being read from
            i += 1
            continue
        else:                                       # create lists for the reformatting of individual data 
            emp_id.append(row[0])
            first_name.append(row[1].split()[0])
            last_name.append(row[1].split()[1])
            dob.append(str(row[2].split('-')[2]) + "/" + str(row[2].split('-')[0]) + "/" + str(row[2].split('-')[1]))
            ssn.append("***-**-" + str(row[3].split('-')[2]))
            state.append(us_state_abbrev[row[4]])

# zip together reformatted data to be rewritten        
newformat_data = zip(emp_id,first_name,last_name,dob,ssn,state)

# Specify the file to write to
output_path = os.path.join("..", "output", "results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Emp ID','First Name', 'Last Name', 'DOB', 'SSN', 'State'])

    # Write the second row onwards
    for row in newformat_data:
        csvwriter.writerow(row)