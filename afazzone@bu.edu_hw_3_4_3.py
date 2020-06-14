# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 20:50:53 2019

@author: alf11
"""

a,b,c,d,e,f = eval(input("Enter a,b,c,d,e,f:"))


if (a*d - b*c) == 0:
    print("The equation has no solution.")
else:
    x = (e*d - b*f)/(a*d - b*c)
    y = (a*f - e*c)/(a*d - b*c)
    print("X is ", x, "and Y is", y)
