# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 10:46:32 2019

@author: alf11
"""
import math

x = [2, 6, -6, -3, 1, 19]

def bubble (x):
    for i in range (0, len(x)):
        for j in range (i+1, len(x)):
            first = x[i]
            second = x[j]
            if first > 0 and second > 0:
                if first > second:
                    first, second = second, first
                    x[i] = first
                    x[j] = second
            elif first < 0 and second < 0:
                if abs(second) > abs(first):
                        first, second = second, first
                        x[i] = first
                        x[j] = second
            elif first < 0 and second > 0:
                  first, second = second, first
                  x[i] = first
                  x[j] = second
    print (x)

bubble(x)


                
            