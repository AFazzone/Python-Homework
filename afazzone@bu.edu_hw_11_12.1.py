# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:32:48 2019

@author: alf11
"""




import math
 
class GeometricObject():
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled
    
    def getColor(self):
        return  self.__color
        
    def isFilled(self):
        return  self.__filled
    
    def setColor(self):
        self.__color = color
        
    def setFilled(self):
        self.__filled = filled
    
    def __str__(self):
        return "Color: " + self.__color + \
            " , Filled: " + str(bool(self.__filled))
 
 
 
class Triangle(GeometricObject):
    def __init__ (self, side1, side2, side3, color, filled):
        GeometricObject.__init__(self, color, filled)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def getSide1(self):
        return self.side1
        
    def getSide2(self):
        return self.side2
        
    def getSide3(self):
        return self.side3
    
    def setSide1(self):
        self.side1 = side1
        
    def setSide2(self):
        self.side2 = side2
 
    def setSide3(self):
        self.side3 = side3
 
    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def getArea(self):
        s = (self.side1 + self.side2 + self.side3)/2
        return math.sqrt(s*((s - self.side1)*(s - self.side2)*
                (s - self.side3)))
    
    def __str2__(self):
        return "Triangle side1 = " + str(self.side1) + ", Triangle side2 = " \
                + str(self.side2) + ", Triangle side3 = " + str(self.side3)
 
def main():
    side1, side2, side3 = eval(input("Enter 3 sides: "))
    color = input("Enter a color: ")
    filled = eval(input("Enter 0 for unfilled or 1 for filled:"))
        
    tri = Triangle(side1, side2, side3, color, filled)
    
    print()
    print(tri.__str__())
    print(tri.__str2__())
    print ("The area of the Triangle is ", round(tri.getArea(),2))
    print ("The Perimeter of the Triangle is ", tri.getPerimeter())
    
        
main()

