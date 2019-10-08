# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:13:32 2019

@author: yigit
"""
i = 0
while i<2:
    while True:
        num1 = int(input('Birinci sayıyı giriniz: '))
        num2 = int(input('İkinci sayıyı giriniz: '))
        op = input("İşlemi giriniz (+ or -): ")
        if op == '-':
            num3 = num1 - num2
        elif op == '+':
            num3 = num1 + num2
        else:
            break
        print(num3)
    i+=1
print('Program bitti')