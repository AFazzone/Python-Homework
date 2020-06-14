# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:22:47 2019

@author: alf11
"""

str = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated"""

def my_print (str, cursor):
    print(str[: cursor] + "^" + str[cursor :])
    
def cmd_n (str, cursor, target):
    new_cur = str.find(target, cursor)
    if new_cur >=0:
        return(new_cur)
    else:
        return(cursor)
        

cursor = 20

my_print(str, cursor)
print()
cursor = cmd_n(str, cursor, "is")
my_print(str, cursor)