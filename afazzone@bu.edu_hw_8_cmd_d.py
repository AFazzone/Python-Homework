# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:30:27 2019

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
    
def cmd_d(str, line, cur):
    left = '\n'.join(str[:line])
    mid = str[line][:cur] 
    right = '\n'.join(str[line+1:])
    print(left + '\n'+  mid + '\n' + '^' + right)
 
my_print(list,2,3)
print()
cmd_d(list, 2, 3)