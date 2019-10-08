# -*- coding: utf-8 -*-

num_tuple = (1, 2, 4, 5, 3, 2, 4, 5, 5, 5, 6, 7)
nums = []

for num in num_tuple:
    if num_tuple.count(num) > 1 and not (num in nums):
        nums.append(num)
        print(num)