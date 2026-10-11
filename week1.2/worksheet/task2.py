# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

list = read_numbers()

if len(list) == 0:
        sys.exit("Error: no numbers provided")

print(f"Minimum = {min(list)}")
print(f"Maximum = {max(list)}")
mean = sum(list)/len(list)
print(f"Mean = {mean}")
list.sort()
middle = round(len(list)/2) - 1
if len(list) % 2 == 1:
        median = list[middle]
if len(list) % 2 == 0:
        median = (list[middle] +list[middle+1])/2
print(f"Median = {median}")