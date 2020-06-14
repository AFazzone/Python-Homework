# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:41:39 2019

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
    
def cmd_n (str,line, cur):
    word = list[line]
    s = word.index("is")
    return (s)

my_print(list,2,3)
print()
cursor =  cmd_n (list, 2,3)
my_print(list, 2, cursor)