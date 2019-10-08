# -*- coding: utf-8 -*-

num = int(input('Sayı giriniz: '))
while not(num == 0):
    word = input('Kelime giriniz: ')
    for index in range(num):
        print(word)
    num = int(input('Sayı giriniz: '))