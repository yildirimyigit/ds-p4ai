# -*- coding: utf-8 -*-

num = int(input())
sum = 0
for index in range(0, num, 2):
    sum = sum + index
print('Toplam: ', str(sum))