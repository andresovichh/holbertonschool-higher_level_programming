#!/usr/bin/python3

import datetime

class User:

    """ A member of ...."""
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday
        # Extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """ REturn the age og the user in years."""
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) # DAte of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)



user = User("Dave Bowman", "19881203")
print(user.age())