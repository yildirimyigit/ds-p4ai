import datetime


class Dog:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
        self.last_vaccination_date = -1

    def vaccinate(self):
        self.last_vaccination_date = datetime.date.today()

    def bark(self):
        print("woof")

    def print_name(self):
        print(self.name)

    def print_age(self, year):
        print(year - self.birth_year)
