# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:13:32 2019

@author: yigit
"""
cont = True
while cont:
    num1 = int(input('Birinci sayıyı giriniz: '))
    num2 = int(input('İkinci sayıyı giriniz: '))
    op = input("İşlemi giriniz (+ or -): ")
    if op == '-':
        num3 = num1 - num2
    else:
        num3 = num1 + num2
    print(num3)
    cont_pref = input("Başka işlem yapmak istiyor musunuz (e/h): ")
    if cont_pref == 'e':
        cont = True
    else:
        cont = False
