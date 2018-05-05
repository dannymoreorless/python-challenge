# Script used to convert employee data 
import os
import csv
#US state abbreviations dictionary
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
directory = os.fsencode('../raw_data')
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    csvpath = os.path.join('..','raw_data', filename)
    #declare empty lists for reformatted data
    emp_id = list()
    first_name = list()
    last_name = list()
    dob = list()
    ssn = list()
    state = list()
    i = 0                                               # serves as a flag to skip labels on csv
    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        for row in csvreader:
            if i == 0:                                  # skip over labels from csv being read from
                i += 1
                continue
            else:                                       #reformat data 
                emp_id.append(row[0])
                first_name.append(row[1].split()[0])
                last_name.append(row[1].split()[1])
                dob.append(str(row[2].split('-')[1]) + "/" + str(row[2].split('-')[2]) + "/" + str(row[2].split('-')[0]))
                ssn.append("***-**-" + str(row[3].split('-')[2]))
                state.append(us_state_abbrev[row[4]])
       
    newformat_data = zip(emp_id,first_name,last_name,dob,ssn,state)

    output_path = os.path.join("..", "output", filename + "_results.csv")
    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Emp ID','First Name', 'Last Name', 'DOB', 'SSN', 'State'])
        for row in newformat_data:
            csvwriter.writerow(row)