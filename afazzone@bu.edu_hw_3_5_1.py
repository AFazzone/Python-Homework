# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 21:49:20 2019

@author: alf11
"""

data = eval(input("Enter an integer (the input ends if it is 0): "))


if data == 0:
    print("You didn't enter any number.")

else:
    positive = 0
    negative = 0
    sum = 0
    while data != 0:    
        if data < 0: 
            negative += 1
            sum = sum + data
            data = eval(input("Enter an integer (the input ends if it is 0): "))
        else:
            positive += 1
            sum = sum + data
            data = eval(input("Enter an integer (the input ends if it is 0): "))
    
  
    """The anwer int the book includes 0 as part of the total, but it is not 
    a included in the calculation for the average"""
    total = positive + negative +1
    average = sum / (positive + negative)
       
    print ("The number of positives is ", positive )    
    print ("The number of negatives is ", negative )    
    print ("The total is ", total )
    print ("The average is ", average )


     