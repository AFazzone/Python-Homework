# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:13:27 2019

@author: alf11
"""

import math

degree = 0


print ("Degree  Sin        Cos")

i = 0

while i < 361:
    print (format(i,"<6d"), end = " ")
    print (format(math.sin(i),">7.4f"), end = " ")
    print (format(math.cos(i), ">10.4f"), end = " ")
    i += 10
    print()