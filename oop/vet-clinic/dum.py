"""
  @author: yigit.yildirim@boun.edu.tr
"""

class VetClinic:
    def __init__(self, name):
        self.name = name
        self.cats = []
        self.dogs = []

    def add_cat(self, cat):
        self.cats.append(cat)

    def add_dog(self, dog_name, dog_by):
        d = Dog(dog_name, dog_by)
        self.dogs.append(d)

    def vaccination_day(self):
        for cat in self.cats:
            cat.vaccinate()
        for dog in self.dogs:
            dog.vaccinate()
        print(len(self.cats)+len(self.dogs))


my_clinic = VetClinic('pati')
my_clinic.add_dog('Comar', 2012)
my_clinic.add_cat(Cat('Tekir', 2018))

c0 = Cat('Sarman', 2019)
my_clinic.add_cat(c0)
my_clinic.vaccination_day()
