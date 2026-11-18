# See README.md for instructions on what to do this program

import random

random.seed(10)

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)

#The random seed value affects all the random, such that they will always get the same results in the same order,if the seed is the same
