# -*- coding: utf-8 -*-

file = open('myfile.txt', 'a')

line0 = '\nIki kere iki dort eder'
line1 = '3 x 2 = 6'

file.write(line0)
file.write('\n')
file.write(line1)

file.close()

'''
file = open('myfile.txt', 'r')

for line in file:
    print(line)
    print('***')

file.close()
'''

file = open('myfile.txt', 'r')

for line in file:
    for s in line.split():
        print(s)

file.close()



















