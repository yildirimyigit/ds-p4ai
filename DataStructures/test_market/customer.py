"""
  @author: yigit.yildirim@boun.edu.tr
"""

import random


class Customer:
    def __init__(self, max_time, max_request):
        self.order = random.randint(0, max_request)
        self.request_time = random.randint(0, max_time)
