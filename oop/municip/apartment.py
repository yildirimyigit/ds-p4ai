from person import Person


class Apartment:
    def __init__(self, num_in, num_rooms, people=[]):
        self.num = num_in
        self.num_rooms = num_rooms
        self.people = people
        self.occupied = False

    def move_in(self, people):
        if not self.occupied:
            return False
        else:
            self.occupied = True
            self.people = people
            return True

