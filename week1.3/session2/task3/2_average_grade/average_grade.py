# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]


# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f

data = []

with open("student_data.csv","r") as file:
    for line in file:
        data.append(line.strip().split(","))
    with open("report.txt","w") as report:
        for i in range (1,len(data)):
            average = (int(data[i][2]) + int(data[i][3]) + int(data[i][4])) / 3
            report.writelines([f"{data[i][1]},{average:.2f}\n"])
