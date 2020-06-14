# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:19:25 2019

@author: alf11
"""

list= ["Beautiful is better than ugly.", 
"Explicit is better than implicit.",
"Simple is better than complex.",
"Complex is better than complicated."]
 
line, cur = 0,0

def my_print(str, line, cur):
    left = '\n'.join(str[:line])
    mid = str[line][:cur] + "^" + str[line][cur:]
    right = '\n'.join(str[line+1:])
    print(left + '\n'+  mid + '\n' + right)

def start_third(x):
    return 2, 0

my_print(list, 1,5)
print()
line, cur = 1,5
line, cur = start_third(list)
my_print(list, line, cur)