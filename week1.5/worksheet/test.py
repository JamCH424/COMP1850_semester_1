import person
from datetime import date

DOB = date(2000, 11, 2)
a = person.Person("Adam",DOB)

print(a.is_birthday())
print(a.initials())