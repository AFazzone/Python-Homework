# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 21:24:16 2019

@author: alf11
"""

print("Kilograms   Pounds")
kilo = 1

while kilo <= 200:
    print(format(kilo,"<9d"), format(kilo*2.2, ">8.1f"))
    kilo += 1