# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:52:00 2019

@author: alf11
"""

tuition = 10000
year = 1

while year < 10:
    tuition = tuition * 1.05
    year += 1

print("Tuition 10 years from now is", '${:,.0f}'.format(tuition))

total = tuition
start = 1

while start <= 3:
    tuition = tuition * 1.05
    total = total + tuition
    start += 1

print("The total for 4 years of tuition starting ten years from now is",
      '${:,.0f}'.format(total))

