# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:21:35 2019

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

def end_first(x):
    return 0, len(x[0])


my_print(list,2,5)
print()
line, cur = 2,5
line, cur = end_first(list)
my_print(list, line, cur)