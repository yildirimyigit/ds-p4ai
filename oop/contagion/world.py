"""
  @author: yigit.yildirim@boun.edu.tr

  Note: I created this class to define the shape of the environment.
  But I haven't implemented any shape other than rectangular yet.
  So this may be improved. Just don't forget to change
  Person.move_towards_goal() to reflect your improvements.
"""
from person import Person


class World:
    def __init__(self, canvas):
        self.points = [0, 0, canvas.winfo_width(), 0, canvas.winfo_width(), canvas.winfo_height(), 0,
                       canvas.winfo_height()]
        self.end_point = (canvas.winfo_width(), canvas.winfo_height())
        self.canvas = canvas
        self.people = []

    def update_points(self):
        self.points = [0, 0, self.canvas.winfo_width(), 0, self.canvas.winfo_width(),
                       self.canvas.winfo_height(), 0, self.canvas.winfo_height()]
        self.end_point = (self.canvas.winfo_width(), self.canvas.winfo_height())

    def run(self, num_indiv, hz):
        for i in range(num_indiv):
            self.people.append(Person(i, self, hz))

        for p in self.people:
            p.move_towards_goal()

    def notify(self, obj_id):
        bbox = self.canvas.bbox(obj_id)
        overlapping = self.canvas.find_overlapping(bbox[0], bbox[1], bbox[2], bbox[3])
        if len(overlapping) > 1:
            for circle_id in overlapping:
                self.people[circle_id-1].conflict()
