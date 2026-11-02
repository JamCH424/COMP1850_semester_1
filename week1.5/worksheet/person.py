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
        if not isinstance(name, str):
                    raise TypeError("name has to be a string")
        if name == "": 
            raise ValueError("Name cannot be empty")

        if not isinstance(birth,date):
            raise TypeError("birth has to be a date object")

        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):
        """
        returns the intials of the person in uppercase and conjoined
        """

        initials = self.name[0].upper()

        for i in range(len(self.name)):
            if self.name[i] == " ":
                initials += self.name[i+1].upper()

        return initials

    def is_birthday(self):
        """
        Checks if it's the person birthday today, boolean variable
        """
        today = date.today()
        if self.birth.month == today.month:
            if self.birth.day == today.day:
                return True
        else:
            return False