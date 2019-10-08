# -*- coding: utf-8 -*-

s = input('String giriniz:\n')
is_different=False
for i in range(int(len(s)/2)):
    if s[i]==s[-i-1]:
        is_different = True
    else:
        is_different = False
        break
print(is_different)