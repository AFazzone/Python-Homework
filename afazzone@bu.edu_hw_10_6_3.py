# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:39:05 2019

@author: alf11
"""

def reverse (number):
    x = str(number)
    x_list = list(x)
    x_list = x_list[::-1]
    return (x_list)

print (reverse (654))

def isPalindrome (number):
    x = str(number)
    x_list = list(x)
    y = reverse(number)
    print(x_list)
    print(y)
    for i in range(len(x_list)):
        if x_list[i] != y[i]:
            print("The number is not a Palindrome")
            Pal = False
            break
        else:
            if x_list[i] == y[i]:
                i += 1
            Pal = True
    if Pal == True:
        print("The number is a Palindrome")
        
print()
isPalindrome (3456789)
print()
isPalindrome (123454321)