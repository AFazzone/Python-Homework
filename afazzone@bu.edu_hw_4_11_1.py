# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 11:15:25 2019

@author: alf11
"""

s1 = []
s2 = []
s3 = []

s1 = eval(input("Enter a 3-by-4 matrix row for row 1: "))
s2 = eval(input("Enter a 3-by-4 matrix row for row 2: "))
s3 = eval(input("Enter a 3-by-4 matrix row for row 3: "))
    
matrix = [s1, s2, s3]


def sumColumn(m, columnIndex):   
    total = 0
    for i in range(len(m)):
        total += matrix[i][columnIndex]       
    return total


for e in range(len(matrix[0])):
    print ("Sum of the elements for column ", e, "is", str(sumColumn(matrix, e)))


