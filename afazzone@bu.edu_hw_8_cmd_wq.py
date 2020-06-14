## -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:33:05 2019

@author: alf11
"""

import pickle

list= ["Beautiful is better than ugly.", 
"Explicit is better than implicit.",
"Simple is better than complex.",
"Complex is better than complicated."]

def cmd_wq (list):
    with open('listfile.txt', 'w') as filehandle:
        for item in list:
            filehandle.write('%s\n' % item)

cmd_wq(list)

