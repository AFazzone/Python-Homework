# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:24:16 2019

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
    
def end_file(x):
    return len(x)-1, len(x[-1])

my_print(list, 2,3)
print()
line,cur = 2,3
line, cur = end_file(list)
my_print(list, line, cur)