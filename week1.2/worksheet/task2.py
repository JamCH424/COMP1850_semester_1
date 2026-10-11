# Worksheet 1.2: Task 2 Solution
import sys

list = []

for i in range(0,5):
    try:
        num = float(input("Enter a number: "))
        list.append(num)
    except:
        sys.exit("Error: no numbers provided")

print("Minimum = ",min(list))
print("Maximum = ",max(list))
mean = sum(list)/len(list)
print("Mean = ",mean)