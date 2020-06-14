# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 18:53:19 2019

@author: alf11
"""


a = "TTCG"
b = "ACGT"
c = "TTAC"
d = "GTAA"


def complementary (x,y):
    x_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    x_list = list(x)
    y_list = list(y)
    z_list = []
    for i in range(len(y_list)):
        y_key = y_list[i]
        z_list.append(x_dict[y_key])
    z_list = z_list[::-1]
    if z_list == x_list :
        print("True")
    else:
        print("False")
        
        
        
complementary(a,b)
complementary(c,d)





     