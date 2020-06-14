# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:02:39 2019

@author: alf11
"""

def displaySortedNumbers (x,y,z):
    x = [x,y,z]
    if x[0] > x[1]:
        x[0], x[1] = x[1], x[0]
    if x[0] > x[2]:
        x[0], x[2] = x[2], x[0]
    if x[1] > x[2]:
        x[1], x[2] = x[2], x[1]
    print("The sorted numbers are", x)
    
displaySortedNumbers(3,2.4,5)