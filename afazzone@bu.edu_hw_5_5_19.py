# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 15:34:51 2019

@author: alf11
"""

lines = eval(input("Enter and interger between 1 and 15:"))

    
for i in range(1, lines + 1):
    for j in range(lines -i, 0,-1):
       print("  ", end = "")           
    for j in range(i, 0, -1):
        print(j, end = " ")
    for j in range(2, i + 1):
        print(j, end = " ")
        

    print()



