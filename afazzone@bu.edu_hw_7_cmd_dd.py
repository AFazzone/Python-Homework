# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:18:53 2019

@author: alf11
"""

str = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated"""

def my_print (str, cursor):
    print(str[: cursor] + "^" + str[cursor :])
    
def cmd_dd (str, cursor):
    if cursor <= 31:
        begin_line = 0
        end_line = str.find("\n", cursor)
    else:
        begin_line = str.rfind("\n",0 ,cursor)
        end_line = str.find("\n", cursor)
    print(str[:begin_line] + "\n" + '^'+ str[end_line +1:])

        

my_print(str, 45)
print()   
cmd_dd (str, 45)
