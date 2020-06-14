# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:07:34 2019

@author: alf11
"""

str = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated"""


def my_print (str, cursor):
    print(str[: cursor] + "^" + str[cursor :])
    
def cmd_x(str, cursor):
    if cursor > 0:
        print(str[: cursor-1] + "^" + str[cursor:])
    else :
        print (str)
  
my_print(str, 9)   
print()
cmd_x (str, 9)

