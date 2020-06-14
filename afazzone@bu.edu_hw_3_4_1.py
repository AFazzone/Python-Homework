# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 21:09:03 2019

@author: alf11
"""

import math

a,b,c = eval(input("Enter a,b,c:"))

discriminant = b**2 -(4*a*c)
print (discriminant)
if discriminant < 0:
    print("The equation has no real roots")
elif discriminant == 0:
    root = (-b + math.sqrt(b**2 -(4*a*c)))/(2*a)
    print("The root is ", root)
else:
    root1 = (-b + math.sqrt(b**2 -(4*a*c)))/(2*a)
    root2 = (-b - math.sqrt(b**2 -(4*a*c)))/(2*a)
    print("The roots are ", root1, root2)
    