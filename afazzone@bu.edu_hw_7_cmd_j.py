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

def cmd_j (str, cursor):
    right_chr = cursor - str.rfind("\n", 0, cursor)
    if cursor <=30:
        return cursor
    else:
        if cursor <= 64:
           return(right_chr)
        elif cursor <=95:
            return(30 + right_chr)
        else:
            return(95 + right_chr)
    
my_print(str, 45)
print()
my_print (str, cmd_j(str, 45))