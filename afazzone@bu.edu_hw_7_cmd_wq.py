# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:37:29 2019

@author: alf11
"""
str = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated"""


def cmd_wq (str):
    outfile = open("Monty.txt", "w")
    outfile.write(str)
    outfile.close()

cmd_wq(str)