# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:31:06 2019

@author: alf11
"""



class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    
    def getA(self):
        return self.__a
 
    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def getD(self):
        return self.__d
 
    def getE(self):
        return self.__e
    
    def getF(self):
        return self.__f
    
    def isSolveable(self):
        if ((self.__a * self.__d) - (self.__b * self.__c)) != 0:
            return True
                
    def getX(self):
        return (((self.__e * self.__d) - (self.__b * self.__f))/
                 ((self.__a * self.__d) - (self.__b * self.__c)))
                 
    def getY(self):
        return (((self.__a * self.__f) - (self.__e * self.__c))/
                 ((self.__a * self.__d) - (self.__b * self.__c)))
                 
def main():    
    a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))
    equation = LinearEquation(a, b, c, d, e, f)
    denominator = equation.isSolveable()
    
    if denominator != True:
        print("The equation has no solution")
    else :
        print("X is ", equation.getX(), "Y is ", equation.getY())
    
main()