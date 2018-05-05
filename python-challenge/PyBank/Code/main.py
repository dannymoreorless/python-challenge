# Script used to analyze financial data for a given period.

import os
import csv

directory = os.fsencode('../raw_data')
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    csvpath = os.path.join('..','raw_data', filename)
    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        total_months = -1                                               # starting at -1 accounts for labels  
        dates = list()
        revenue = list()
        for row in csvreader:
            total_months += 1                                           # Find number of data points given in the data set
            dates.append(row[0])                                        # create a list of the dates
            revenue.append(row[1])                                      # create a list of the revenues
        dates.remove("Date")
        revenue.remove("Revenue")
        total_revenue = int(revenue[0])  
        rev_change_sum = 0
        revenue_change = list()
        previous = int(revenue[0])
        for rev in revenue[1:]:                                         
            total_revenue += int(rev)
            revenue_change.append(int(rev)-previous)                    #calculate revenue change and append to list of revenue changes
            rev_change_sum += int(rev)-previous                         #calc sum of revenue changes to be used in average revenue change calc
            previous = int(rev)                                         #update previous variable
            if (len(revenue_change) == len(revenue) - 1):               
                break
        #Find Avg Revenue Change
        avg_rev_change = round(rev_change_sum/len(revenue_change),2)    #Calculate average for revenue changes over period
        #Finds Max & Min revenue change for data set
        greatest_inc =  max(revenue_change)                             
        greatest_dec =  min(revenue_change)                             
        g_inc_date = dates[revenue_change.index(greatest_inc)+1]        
        g_dec_date = dates[revenue_change.index(greatest_dec)+1]        
    output_path = os.path.join("..", "output", filename + "_results.txt")
    file = open(output_path, "w")
    file.write("Financial Analysis from " + filename + "\n------------------------\n")
    file.write("Total Months:\t" + str(total_months) + "\nTotal Revenue:\t$" + str(total_revenue) +"\nAverage Revenue Change: $" + str(avg_rev_change) + "\nGreatest Increase in Revenue: " + g_inc_date + " ($" + str(greatest_inc) + ")\nGreatest Decrease in Revenue: " + g_dec_date + " ($" + str(greatest_dec) + ")\n") 
    file.close()
    print("\n----------------------------\nFinancial Analysis from " + filename + "\n------------------------\n")
    print("Total Months:\t" + str(total_months) + "\nTotal Revenue:\t$" + str(total_revenue) +"\nAverage Revenue Change: $" + str(avg_rev_change) + "\nGreatest Increase in Revenue: " + g_inc_date + " ($" + str(greatest_inc) + ")\nGreatest Decrease in Revenue: " + g_dec_date + " ($" + str(greatest_dec) + ")\n\n----------------------------\n") 

