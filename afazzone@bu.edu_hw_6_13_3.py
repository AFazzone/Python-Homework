# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:55:11 2019

@author: alf11
"""

def main():
    f1 = input("Enter a filename: ").strip()
 
    infile = open(f1, "r")
    
    s = infile.read() 
    list = (s.split(" "))
    list = [int(i) for i in list]
    total = 0
    scores = len(list)
    
    for e in list:
        total += e
    
    print("There are", scores,"scores.") 
    print("The total is :", total)
    print("The average is :" , round(total/scores, 2))
    
    infile.close() 

main()