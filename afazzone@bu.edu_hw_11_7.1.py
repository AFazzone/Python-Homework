# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 22:13:37 2019

@author: alf11
"""
 
class Rectangle:
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height
    
    def getHeight(self):
        return self.height  

    def getWidth(self):
        return self.width    
    
    def getPerimeter(self):
        return 2*self.width + 2*self.height
        
    def getArea(self):
        return self.width * self.height
 
x = Rectangle(4,40)
print ("Width is ", x.getWidth())
print ("Height is ", x.getHeight())
print ("Area is ", x.getArea())
print ("Perimeter is ", x.getPerimeter())
 
print()
 
y = Rectangle(3.5,35.7)
print ("Width is ", y.getWidth())
print ("Height is ", y.getHeight())
print ("Area is ", round(y.getArea(),2))
print ("Perimeter is ", y.getPerimeter())