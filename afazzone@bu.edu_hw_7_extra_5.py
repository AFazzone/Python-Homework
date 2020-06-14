# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:56:43 2019

@author: alf11
"""

str = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated"""


def my_print (str, cursor):
    print(str[: cursor] + "^" + str[cursor :])
    
def delete_right(str, cursor):
    if cursor > 0:
        print(str[: cursor] + "^" + str[cursor +1:])
    else :
        print (str)
  
my_print(str, 14)   
print()
delete_right (str, 14)
