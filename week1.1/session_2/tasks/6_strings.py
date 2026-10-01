# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") #Prints the original string
print(f"Modified String 1: {user_string.lower()}") #Prints the string as lower letters
print(f"Modified String 2: {user_string.upper()}") #Prints the string as Uppercase/capital letters
print(f"Modified String 3: {user_string.strip()}") #Remove all spaces before the first non-space and after the last non-space.
print(f"Modified String 4: {user_string.replace('a', '@')}") #replaces all a in the string into @
print(f"Modified String 5: {user_string.capitalize()}") #Caplitalize the first letter and sets all other letters to lowercase
print(f"Modified String 6: {user_string[::-1]}") #Inverts / mirror the string
print(f"Modified String 7: {user_string.title()}") #Capitilize the first letter and sets all other letter to lowercase
print(f"Modified String 8: {len(user_string)}") #Ouput the length of the string
print(f"Modified String 9: {user_string.find('a')}") #Ouput the posistion of the first a in the string
print(f"Modified String 10: {user_string.count('a')}") #Ouput the number a are in the string
print(f"Modified String 11: {user_string.startswith('Hello')}") #Boolean, Checks if the string begins with "Hello"
print(f"Modified String 12: {user_string.endswith('!')}") #Boolean, Checks if the string ends with "!"
print(f"Modified String 13: {user_string.isalnum()}") #Boolean, Checks if the string is made of digits and the alphabet/ letters
print(f"Modified String 14: {user_string.isalpha()}") #Boolean, Checks if the string is made of alphabet/ letters
print(f"Modified String 15: {user_string.isdigit()}") #Boolean, Checks if the string isa digit



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!