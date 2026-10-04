"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.


try:
    save_per_month = int(input("How much money do you want to save?: "))
    running = False
except:
    print("\nInvalid amount\n")


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.

money_saved_per_year = save_per_month * 12
print(f"You will save {money_saved_per_year} by the end of the year if you save {save_per_month} every month.")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

money_saved_per_year_and_interest = float(money_saved_per_year * 1.008)
print(f"Including interest that is £{money_saved_per_year_and_interest:.2f}!")