# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format

largest_sale_amount = 0
count = 0
total = 0
most_sold_unit = 0
west_total = 0
east_total = 0
north_total = 0
south_total = 0
west_most_sold_unit = 0
north_most_sold_unit = 0
east_most_sold_unit = 0
south_most_sold_unit = 0

with open("sales.csv","r") as infile:
    for line in infile:
        data = line.strip().split(",")
        if data[2].isdigit() == True:
            if int(data[2]) > largest_sale_amount:
                largest_sale_amount = int(data[2])
                largest_sale_day = data[0]
            total =+ int(data[2])
            count =+ 1
        if data[3].isdigit() == True:
            if int(data[3]) > most_sold_unit:
                most_sold_unit = int(data[3])
                most_sold_widget = data[1]
        if data[4] == "West":
            west_total =+ int(data[2])
            if data[3].isdigit() == True:
                if int(data[3]) > west_most_sold_unit:
                    west_most_sold_unit = int(data[3])
                    west_most_sold_widget = data[1]
        if data[4] == "North":
                    west_total =+ int(data[2])
                    if data[3].isdigit() == True:
                        if int(data[3]) > north_most_sold_unit:
                            north_most_sold_unit = int(data[3])
                            north_most_sold_widget = data[1]
        if data[4] == "East":
                    east_total =+ int(data[2])
                    if data[3].isdigit() == True:
                        if int(data[3]) > east_most_sold_unit:
                            east_most_sold_unit = int(data[3])
                            east_most_sold_widget = data[1]
        if data[4] == "South":
                    south_total =+ int(data[2])
                    if data[3].isdigit() == True:
                        if int(data[3]) > south_most_sold_unit:
                            south_most_sold_unit = int(data[3])
                            south_most_sold_widget = data[1]

mean = total/count
print(f"The largest amount of sales is {largest_sale_amount} made on {largest_sale_day}")      
print(f"The average sales amount per day is {mean}") 
print(f"The most sold widget is {most_sold_widget} with {most_sold_unit} units sold")

print(f"The total sales for the west region is {west_total}")
print(f"The total sales for the east region is {east_total}")
print(f"The total sales for the north region is {north_total}")
print(f"The total sales for the south region is {south_total}")

print(f"The most sold widget in the west is {west_most_sold_widget} with {west_most_sold_unit} units sold")
print(f"The most sold widget in the west is {east_most_sold_widget} with {east_most_sold_unit} units sold")
print(f"The most sold widget in the west is {north_most_sold_widget} with {north_most_sold_unit} units sold")
print(f"The most sold widget in the west is {south_most_sold_widget} with {south_most_sold_unit} units sold")


# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows