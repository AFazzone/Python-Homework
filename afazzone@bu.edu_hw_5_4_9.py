# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 13:24:56 2019

@author: alf11
"""

pk1_w, pk1_p = eval(input("Enter a weight and price for package 1: "))
pk2_w, pk2_p = eval(input("Enter a weight and price for package 2: "))

pk1_price_per = pk1_p / pk1_w
pk2_price_per = pk2_p / pk2_w

if pk1_price_per < pk2_price_per:
    print ("Package 1 is better")
elif pk1_price_per > pk2_price_per:
    print ("Package 2 is better")
else:
    print ("Both packages are the same")