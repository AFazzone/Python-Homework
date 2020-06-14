# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:18:57 2019

@author: alf11
"""

str = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated"""

def my_print (str, cursor):
    print(str[: cursor] + "^" + str[cursor :])

def cmd_h (str, cursor):
    if cursor > 0:
        return (cursor - 1)
    else:
        return (cursor)

my_print(str,5)
print()
my_print(str, cmd_h(str,5))
print()
