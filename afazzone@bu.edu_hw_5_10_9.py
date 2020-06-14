# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:47:39 2019

@author: alf11
"""
import math


list = []
list = eval(input("Enter a list of numbers:"))

def mean (x):
    sum = 0
    for i in range(len(x)):
        sum = sum + x[i]
    result = sum/len(x)
    return round(result, 2)

print ("The mean is ", mean(list))

def deviation (x):
    sum = 0
    for i in range(len(x)):
        sq_dist = ((x[i] - mean(x))**2)
        sum = sum + sq_dist     
    result = math.sqrt((sum)/(len(x) - 1))
    return round(result, 5)

print("The standard deviation is ", deviation(list))
