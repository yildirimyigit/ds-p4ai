# -*- coding: utf-8 -*-

num = int(input())
sum = 0
for index in range(num):
    sum = sum + index
    print('sum='+str(sum))
print('Toplam: ', str(sum))