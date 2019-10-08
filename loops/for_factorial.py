# -*- coding: utf-8 -*-

num = int(input())
fact = 1
for index in range(num):
    fact = fact * (index+1)
print('Faktöriyel: ', str(fact))