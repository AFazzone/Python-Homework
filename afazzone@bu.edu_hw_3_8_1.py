# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 22:02:07 2019

@author: alf11
"""

ssn = input("Enter a number in format ddd-dd-ddd: ")

ssn_list = ssn.split("-")

if ssn_list[0].isnumeric() and ssn_list[1].isnumeric() \
    and ssn_list[2].isnumeric():
        print("Valid SSN")
else:
    print("Invalid SSN")