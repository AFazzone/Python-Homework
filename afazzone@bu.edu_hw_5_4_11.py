# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 13:38:33 2019

@author: alf11
"""

month, year = eval(input("Enter a month and a year: "))

dict = {1 : "January", 2 : "February", 3 : "March", 4 : "April", 5 : "May",
        6 : "June", 7: "July", 8 : "August", 9 : "Septmeber", 10 : "October",
        11 : "November", 12: "December"}

list_31 = [1,3,5,7,8,10,12]
list_30 = [4,6,9,11]

leap = year % 4

if month in list_31:
    print (dict[month], year, "has 31 days")
elif month in list_30:
    print (dict[month], year, "has 30 days")
elif leap == 0:
    print (dict[month], year, "has 29 days")
else:
    print (dict[month], year, "has 28 days")