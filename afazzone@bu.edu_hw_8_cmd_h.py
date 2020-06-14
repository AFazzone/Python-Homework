# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:06:39 2019

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
    
def cmd_h(str, line, cur):
    if cur < len(str[line]):
        cur -= 1
        return line, cur
    else:
        line -= 1
        cur = len(str[line])
        return line, cur
 
my_print(list, 2,3)
print()
line, cursor = cmd_h(list, 2, 3)
my_print(list, line, cursor)