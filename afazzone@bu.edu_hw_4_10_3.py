# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:40:59 2019

@author: alf11
"""

def main():
    s = input("Enter integers between 1 and 100: ")
    s_list = s.split(",")
    
    dictionary = {} # Create an empty dictionary
    
    for number in s_list:
        if number in dictionary:
            dictionary[number] += 1
        else:
            dictionary[number] = 1
            
    
    for x in dictionary:
        if dictionary[x] == 1:
            print(x, "occurs", dictionary[x], "time")
        else:
            print(x, "occurs", dictionary[x], "times")
        
main()