# Import Modules for Reading raw data
import os
import csv

# Set path for file
csvpath = os.path.join('raw_data','employee_data1.csv')

# Lists to store data
new_employee_data = []

# Open and read the raw data into dictionary
with open(csvpath, newline ="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    for row in csvreader:
        
        # Split first and last name by space
        First_Name = row["Name"].split(" ")[0]
        Last_Name = row["Name"].split(" ")[1]

        # import datetime to reformat DOB
        from datetime import datetime
        DOB = datetime.strptime(row["DOB"], '%Y-%m-%d').strftime('%m/%d/%y')
        
        # import regex to rewrite SSN numbers and hide the first 5 numbers
        import re
        SSN=re.sub("^\d{3}-?\d{2}-?\d{4}", "XXX-XX-",row["SSN"])+row["SSN"][7:11]

        # list orginal state full name as state_full and state abbreviation as state_abbrev
        State_Full = row["State"]
        State_Abbrev = {
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
        
        # import regex to replace state list by state abbrev dictionary
        import re
        pattern = re.compile('|'.join(State_Abbrev.keys()))
        State = pattern.sub(lambda i: State_Abbrev[i.group()], State_Full)

        # Store new data
        new_employee_data.append({"First Name":First_Name,"Last Name":Last_Name, "DOB":DOB, "SSN":SSN,"State":State})

# Write updated data to csv file
csvpath = os.path.join("New_Employee_Data.csv")
with open(csvpath, "w") as csvfile:
    fieldnames = ["First Name", "Last Name", "DOB", "SSN", "State"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_employee_data)