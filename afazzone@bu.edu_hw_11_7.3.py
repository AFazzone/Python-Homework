# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:24:28 2019

@author: alf11
"""

class Account:
    def __init__(self, id = 0, balance = 100, annualInterestRate = 0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
        
    def getId(self):
        return self.__id 
    
    def getBalance(self):
        return self.__balance
        
    def getAnnual(self):
        return self.__annualInterestRate
    
    def setId(self):
        self.__id = id
    
    def setBalance(self):
        self.__balance = balance
        
    def setAnnual(self):
        self.__annualInterestRate = annualInterestRate
        
    def setWithdraw(self, x):
        self.__balance = self.__balance - x
        
    def setDeposit(self, x):
        self.__balance = self.__balance + x
 
    def getMonthlyInterestRate(self):
        return (self.__annualInterestRate/12)/100
        
    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()
 
x = Account(1122, 20000, 4.5)
 
new_bal = x.setWithdraw(2500)
new_bal  = x.setDeposit(3000)
 
print("ID: " , x.getId())
print("Balance: ",  x.getBalance())
print("Monthly Interest Rate: ", x.getMonthlyInterestRate()*100)
print("Monthly Interest: ", x.getMonthlyInterest())