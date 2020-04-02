"""
  @author: yigit.yildirim@boun.edu.tr
"""


class MyStack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        elem = self.data[-1]
        del self.data[-1]
        return elem
