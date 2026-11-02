# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth):
        """
        name is the name of the person, birth is the date of birth
        """

        if name == None:
            raise ValueError("Name cannot be empty")
        if not isinstance(name, str):
            raise TypeError("name has to be a string")

        if not isinstance(birth,date):
            raise TypeError("birth has to be a date object")

        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials():
        """
        returns the intials of the person in uppercase and conjoined
        """

        intials = ""
        for i in range (len(self.name)):
            if self.name[i] == " ":
                intials.append(self.name[i+1].upper())

        return intials

    def is_birthday():
        """
        Checks if it's the person birthday today, boolean variable
        """
        if self.birth == date.date.today():
            return True
        else:
            return False