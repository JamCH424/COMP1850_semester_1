"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""

destination = input("Where are you going to? ")

distance_miles_input = int(input("How many miles will you travel? "))
time_hours_input = int(input("How many hours will the journey take? "))

avg_speed = float(distance_miles_input / time_hours_input)
print(f"Your journey to {destination} will have an average speed of {avg_speed:.2f} mile per hour")
if avg_speed <= 0:
    print("Something went wrong, average speed is below 0 mile per hour")

# TODO: convert distance_miles_input and time_hours_input to numbers
# TODO: calculate the average speed in miles per hour
# TODO: print a summary message using an f-string
# Extension: add validation for zero or negative values
