# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
height = 1.75
weight = 80
bmi = weight/height**2
a = bmi > 25
print(bmi)

if(a is True):
    print('Diyete baslamalisin')
else:
    print('Devam')
