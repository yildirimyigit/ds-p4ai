# -*- coding: utf-8 -*-

inp = input('Cumle giriniz: \n')

ind = inp.find('x')
print(ind)  # soldan

if ind>=0:
    print(len(inp) - ind)   # sagdan