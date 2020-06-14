# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:30:30 2019

@author: alf11
"""

str = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated"""

def my_print (str, cursor):
    print(str[: cursor] + "^" + str[cursor :])

def start (str):
    return(0)

my_print (str, 7)
print()
my_print(str, start(str))