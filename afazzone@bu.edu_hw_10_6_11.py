# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 09:54:27 2019

@author: alf11
"""

def computeCommission (sale):
    print("Sales Amount         Commission")
    for i in sale:
        if i <= 5000:
            com = i * .08
        elif 5000 < i <= 10000:
            com = i *.1
        else:
            com = i *.12
        print(format(i,"<10d"), format(com, ">20.0f"))

x = list(range(5000, 120001, 5000))

computeCommission (x)

""" The exercise that it referenced in 5.39 had the values of 8% up to 5k, 
10% up to 10K, and 12% above that.  However the example print out in the 
book for 6.11 did not correspond to that model, it went from 9% for 10K up to 
11.7% for 100K.  I used the values from 5.39 in my code per the 
instructions and gave examples ranging from 5k to 120K 
to cover all of the increments""" 
