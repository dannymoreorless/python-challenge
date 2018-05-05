# Written by: Daniel Morales
# Script used to analyze financial data for a given period.

# Import needed modules
import os
import csv
#Establish path to csv file of interest
file = input("What file would you like to analyze?\n\tPotential Options:\n\tbudget_data_1.csv\n\tbudget_data_2.csv\n------------------------\n")

csvpath = os.path.join('..','raw_data', file)

#read csv file
with open(csvpath, newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    total_months = -1                                               # starting at -1 accounts for labels  
    dates = list()
    revenue = list()
    for row in csvreader:
        total_months += 1                                           # Find number of data points given in the data set
        dates.append(row[0])                                        # create a list of the dates
        revenue.append(row[1])                                      # create a list of the revenues

    #Clean data by dropping headers
    dates.remove("Date")
    revenue.remove("Revenue")

    #Find total revenue and Revenue changes
    total_revenue = int(revenue[0])  
    rev_change_sum = 0
    revenue_change = list()
    previous = int(revenue[0])
    for rev in revenue[1:]:                                         #Skip first element (no previous data point to calculate change)
        total_revenue += int(rev)
        revenue_change.append(int(rev)-previous)                    #calculate revenue change and append to list of revenue changes
        rev_change_sum += int(rev)-previous                         #calc sum of revenue changes to be used in average revenue change calc
        previous = int(rev)                                         #update previous variable
        if (len(revenue_change) == len(revenue) - 1):               #ends for loop at last element in array
            break
    
    #Find Avg Revenue Change
    avg_rev_change = round(rev_change_sum/len(revenue_change),2)             #Calculate average for revenue changes over period
    
    #Find Max & Min revenue change for data set
    greatest_inc =  max(revenue_change)                             #Finds greatest increase
    greatest_dec =  min(revenue_change)                             #Finds greatest decrease
    g_inc_date = dates[revenue_change.index(greatest_inc)+1]        #Finds date associated with greatest increase
    g_dec_date = dates[revenue_change.index(greatest_dec)+1]        #Finds date associated with greatest decrease

# Set output path for output text file
output_path = os.path.join("..", "output", "results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
file = open(output_path, "w")

#write results into text file
file.write("Financial Analysis\n------------------------\n")
file.write("Total Months:\t" + str(total_months) + "\nTotal Revenue:\t$" + str(total_revenue) +"\nAverage Revenue Change: $" + str(avg_rev_change) + "\nGreatest Increase in Revenue: " + g_inc_date + " ($" + str(greatest_inc) + ")\nGreatest Decrease in Revenue: " + g_dec_date + " ($" + str(greatest_dec) + ")\n") 

#close file
file.close()



