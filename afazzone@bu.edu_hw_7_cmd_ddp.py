# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:22:46 2019

@author: alf11
"""

str = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated"""

def my_print (str, cursor):
    print(str[: cursor] + "^" + str[cursor :])
    

def cmd_ddp (str):
    str2 = str.split("\n")
    print (str2[1] + "\n" + "^"  + str2[0] + "\n" + str2[2] + "\n" + str2[3])

my_print(str,0)
print()
cmd_ddp (str)
