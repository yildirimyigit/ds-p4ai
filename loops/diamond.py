# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:57:47 2019

@author: yigit
"""

a = input('Karakter: \n')
size = int(input("Boyut: \n"))
for i in range(size):
    for x in range(size-i-1):
        print(' ', end = '')
    for x in range(2*i +1):
        print(a , end='')
    print()

for i in range(size):
    '''
    for x in range(i):
        print(' ', end='')
    for x in range((size-i)*2-1):
        print(a, end='')
        '''
    print(' '*i, end='')
    print(a*((size-i)*2-1))
    #print()
    
    
    
    
    
    
    
    
    
