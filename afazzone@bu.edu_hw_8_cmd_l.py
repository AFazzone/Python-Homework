# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:54:20 2019

@author: alf11
"""

list= ["Beautiful is better than ugly.", 
"Explicit is better than implicit.",
"Simple is better than complex.",
"Complex is better than complicated."]

def my_print(str, line, cur):
    left = '\n'.join(str[:line])
    mid = str[line][:cur] + "^" + str[line][cur:]
    right = '\n'.join(str[line+1:])
    print(left + '\n'+  mid + '\n' + right)
 
line, cur = 0,0

def cmd_l(str, line, cur):
    if cur < len(str[line]):
        cur += 1
        return line, cur
    else:
        line += 1
        cur = 0
        return line, cur
my_print(list, 2,3)
print()
line, cur = cmd_l(list, 2, 3)
my_print(list,line, cur)