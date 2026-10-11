# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

list = read_numbers()

if len(list) == 0:
        sys.exit("Error: no numbers provided")

print("Minimum = ",min(list))
print("Maximum = ",max(list))
mean = sum(list)/len(list)
print("Mean = ",mean)