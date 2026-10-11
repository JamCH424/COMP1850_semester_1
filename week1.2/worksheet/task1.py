# Worksheet 1.2: Task 1 Solution
import sys

try:
    num = int(input("Enter an integer grade in the range 0 to 100: "))
    if 39 >= num >= 0:
        print(f"{num} is a Fail")
    elif 69 >= num >= 40:
        print(f"{num} is a Pass")
    elif 100 >= num >= 70:
        print(f"{num} is a Distinction")
    elif num > 100 or 0 < num:
        sys.exit("Error: Grade must be an integer between 0 and 100")
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")