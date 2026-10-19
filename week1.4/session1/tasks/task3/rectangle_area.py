
# function implementation

def rectangle_area(length,height):  # define suitable input data
    area = length * height
    return area              # return an appropriate value

# testing the function

print(f"Area is {rectangle_area(5,10)}")   # provide suitable data matching your inputs

def even_numbers_to(num):
    even_numbers = []
    for i in range (0,num+1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

print(even_numbers_to(10))

def calc_mean(list):
    sum = 0
    for num in list:
        sum += num
    mean = sum / len(list)
    return mean

print(calc_mean(even_numbers_to(10)))