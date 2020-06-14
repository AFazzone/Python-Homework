# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:26:35 2019

@author: alf11
"""



import math
 
class RegularPolygon:
    def __init__ (self, n=3, side=1, x=0, y=0,):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
    
    def getN(self):
        return self.__n
        
    def getSide(self):
        return self.__side
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
        
    def setN(self):
        self.__n = n
        
    def setSide(self):
        self.__side = side
    
    def setX(self):
        self.__x = x
    
    def setY(self):
        self.__y  = y
        
    def getPerimeter(self):
        return self.__side* self.__n
    
    def getArea(self):
        return (self.__n * (self.__side**2))/(4 * math.tan(math.pi/self.__n))
 
def main():
    poly_1 = RegularPolygon()
    poly_2 = RegularPolygon(6, 4)
    poly_3 = RegularPolygon(10, 4, 5.6, 7.8)
 
    print ("The perimeter is ", poly_1.getPerimeter())
    print ("The area is ", round(poly_1.getArea(),2))
    print()
    print ("The perimeter is ", poly_2.getPerimeter())
    print ("The area is ", round(poly_2.getArea(),2))
    print()
    print ("The perimeter is ", poly_3.getPerimeter())
    print ("The area is ", round(poly_3.getArea(),2))
 
main()