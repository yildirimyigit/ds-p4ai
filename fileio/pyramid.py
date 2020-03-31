# -*- coding: utf-8 -*-

char = input("Yan üçgenin karakterini giriniz:\n")
size = int(input("Yüksekliğini giriniz:\n"))

for i in range(size):
    print(char*(i+1))

print(char*(size+1))

for i in range(size):
    print(char*(size-i))