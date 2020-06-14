# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 18:12:13 2019

@author: alf11
"""


lines = 8

list = [1]
count = 1   

for e in range(lines):
    count = count * 2
    list.append(count)


for i in range(1, lines + 1):
    for j in range(lines - i, 0, -1): #  spaces
        print("  ", end = "")
    for j in range(i, 0, -1):         # left triangle 8 bottom
        print(list[i-j], end = " ")
    for j in range(i-1, 0, -1):       # Right triangle7 bottom
        print(list[j-1], end = " ")
    print()

