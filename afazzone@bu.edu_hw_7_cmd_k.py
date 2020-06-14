# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:26:25 2019

@author: alf11
"""

str = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated"""



def my_print (str, cursor):
    print(str[: cursor] + "^" + str[cursor :])



def cmd_k (str, cursor):
    right_chr = cursor - str.rfind("\n", 0, cursor)
    if cursor >= 95:
        return cursor
    else:
        if cursor >= 64:
           return(right_chr + 95)
        elif cursor >=30:
            return(64 + right_chr)
        else:
            return(30 + right_chr)
    

my_print(str, 77)
print()
my_print (str, cmd_k(str, 77))