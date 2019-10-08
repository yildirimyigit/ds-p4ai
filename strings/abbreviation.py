# -*- coding: utf-8 -*-

inp = input('Kurum adi giriniz: \n')
words = inp.split(' ')

result = ''
for word in words:
    result += word[0]
    
print(result)