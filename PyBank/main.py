# Import Modules for Reading raw data
import os
import csv

# Set path for file
csvpath = os.path.join('raw_data','budget_data_1.csv')

# Lists to store data
Month = []
Revenue = []

# Open and read the CSV, excluding header
with open(csvpath, newline="") as csvfile:
    next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:

        # Add Month data to the list
        Month.append(row[0])

        # Add Revenue data to the list
        Revenue.append(int(row[1]))


# Count total number of months
Months_count = len(Month)

# Sum up total amount of Revenue
Revenue_total = sum(Revenue)

# Change in revenue between months
Revenue_change = [Revenue[i+1]-Revenue[i] for i in range(len(Revenue)-1)]

# Average change over the entire period
Average_revenue_change = sum(Revenue_change)/len(Revenue_change)

# The greatest increase in revenue
Greatest_increase = max(Revenue_change)

# Locate the month where has the greatest increase
Index_max = Revenue_change.index(max(Revenue_change))+1
Greatest_increse_month = Month[Index_max]

# The greatest decrese in revenue
Greatest_decrease = min(Revenue_change)

# Locate the month where has the greatest decrease
Index_min = Revenue_change.index(min(Revenue_change))+1
Greatest_decrese_month = Month[Index_min]

# Print the Result
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(Months_count))
print("Total Revenue: $" + str(Revenue_total))
print("Average Revenue Change: $"+str(Average_revenue_change))
print("Greatest Increase in Revenue: "+str(Greatest_increse_month)+" ($"+ str(Greatest_increase)+")")
print("Greatest Decrease in Revenue: "+str(Greatest_decrese_month)+" ($"+ str(Greatest_decrease)+")")

# Export Text File
with open("output_analysis.txt", "w+") as f:
    f.write("Financial Analysis"+"\n")
    f.write("----------------------------"+"\n")
    f.write("Total Months: " + str(Months_count)+"\n")
    f.write("Total Revenue: $" + str(Revenue_total)+"\n")
    f.write("Average Revenue Change: $"+str(Average_revenue_change)+"\n")
    f.write("Greatest Increase in Revenue: "+str(Greatest_increse_month)+" ($"+ str(Greatest_increase)+")"+"\n")
    f.write("Greatest Decrease in Revenue: "+str(Greatest_decrese_month)+" ($"+ str(Greatest_decrease)+")"+"\n")
    f.close()
