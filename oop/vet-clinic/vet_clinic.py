from person import Person


class VetClinic:
    def __init__(self, name, people=[]):
        self.name = name
        self.people = people
        self.total_vaccinated = 0
    def register_client(self, p):
        self.people.append(p)

    def vaccination_day(self):
        for person in self.people:
            for cat in person.cat_list:
                cat.vaccinate()
                self.total_vaccinated +=1
            for dog in person.dog_list:
                dog.vaccinate()
                self.total_vaccinated +=1