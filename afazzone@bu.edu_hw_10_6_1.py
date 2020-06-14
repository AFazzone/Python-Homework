# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:17:03 2019

@author: alf11
"""

def getPentagonalNumber(n):
    for i in range (1, 11):
        print('\n')
        for j in range (1,11):
            pent = n*(3*n - 1)/2
            print (int(pent), end = " ")
            n +=1
        
getPentagonalNumber(1)