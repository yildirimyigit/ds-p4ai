from cat import Cat
from dog import Dog


class Person:
    def __init__(self, name, cat_list=[], dog_list=[]):
        self.name = name
        self.cat_list = cat_list
        self.dog_list = dog_list

    def cat_add(self, name, by):
        c = Cat(name, by)
        self.pet_list.append(c)

    def dog_add(self, name, by):
        d = Dog(name, by)
        self.pet_list.append(d)


p0 = Person('omar', [])
p0.cat_add('mirmir', 2015)
p0.dog_add('kucukucu', 2017)
print(p0.pet_list)