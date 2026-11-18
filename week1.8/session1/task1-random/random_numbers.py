import random

# Get user to input how many random numbers they want

# Generate this many random numbers

# Write the random numbers to a file named random.txt, one number per line

num = int(input("How many random inputs do you want?: "))

with open("RandomNumbers.txt", "w") as f:
    for i in range(num):
        RandomNumber = random.random()
        print(RandomNumber)
        f.write(str(RandomNumber) + "\n")