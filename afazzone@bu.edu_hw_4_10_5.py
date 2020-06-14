# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:16:43 2019

@author: alf11
"""

a,b,c,d,e,f,g,h,i,j = eval(input("Enter ten numbers: "))
x_list = [a,b,c,d,e,f,g,h,i,j]
y_list = []

for i in x_list:
    if i not in y_list:
        y_list.append(i)
        
print("The distinct numbers are :", str(y_list).strip('[]'))