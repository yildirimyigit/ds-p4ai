"""
  @author: yigit.yildirim@boun.edu.tr
"""

import random


class Producer:
    def __init__(self, max_daily_cap):
        self.daily_capacity = random.randint(0, max_daily_cap)
