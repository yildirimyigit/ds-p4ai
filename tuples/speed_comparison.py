# -*- coding: utf-8 -*-

import time

l = []

for i in range(10000000):
    l.append(i)

t = tuple(l)


ts = time.time()
s = sum(l)
e = time.time()
print(e - ts)
print('xxxxx')
ts = time.time()
s = sum(t)
e = time.time()
print(e - ts)