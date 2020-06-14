# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:59:53 2019

@author: alf11
"""

INFO = 0; NEXT_PTR = 1; PREV_PTR = 2;
 
 
str="""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""
 
def create_node(data):
    return[data, None, None]
 
def create_double(str):
    list = str.split('\n')
    start = None; last = None
    for line in list:
        n_node = [line, None, None]
        if start is None:
            start = n_node
            last = n_node
        else:
            n_node[PREV_PTR] = last
            last[NEXT_PTR] = n_node
            last = n_node
    return(start, last)
 
 
start, last = create_double(str)
cur_node = start; 

def my_print(start, last, cur_node, pos):
    next_node = start
    while next_node != cur_node:
        print(next_node[INFO])
        next_node = next_node[NEXT_PTR]
    n_str = cur_node[INFO]
    print(n_str[0:pos] + '^' + n_str[pos:])
    if cur_node != last:
        n_node = cur_node[NEXT_PTR]
        while n_node != None:
            print(n_node[INFO])
            n_node = n_node[NEXT_PTR]

def right_3(start,last,cur_node, pos)    :
    cur_line = cur_node[INFO]
    if pos != 0:
        pos = pos + 3
        return pos
    
pos = 8
my_print(start,last,cur_node,pos)
print()
my_print(start,last,cur_node,right_3(start,last,cur_node,pos))