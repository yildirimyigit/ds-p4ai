# -*- coding: utf-8 -*-

inp_str = input('Sayı giriniz: ')
pow = int(inp_str)
i = 0
while pow < 1000:
    pow = pow**i
    i = i+1