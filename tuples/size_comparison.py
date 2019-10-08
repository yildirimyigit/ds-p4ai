# -*- coding: utf-8 -*-

l = list(range(0,1000))
t = tuple(l)

print('list=',l.__sizeof__())
print('tuple=',t.__sizeof__())