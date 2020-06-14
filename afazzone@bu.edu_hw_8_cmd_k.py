# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:21:52 2019

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
    
def cmd_k(str, line, cur):
    if len(str[line - 1]) >= cur:
        line, cur = line+1, cur
        return line, cur
    else:
        line, cur = line +1, len(str[line - 1])
        return line, cur
 
my_print(list, 2,7)
print()
line, cursor = cmd_k(list, 2, 7)
my_print(list, line, cursor)