# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:16:16 2019

@author: alf11
"""

str = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated"""

def my_print (str, cursor):
    print(str[: cursor] + "^" + str[cursor :])


def cmd_d (str, cursor):
    end_line = str.find("\n")
    print(str[: cursor] + "^" + str[end_line:])
 
    
my_print(str, 8)   
print()
cmd_d (str, 8)
