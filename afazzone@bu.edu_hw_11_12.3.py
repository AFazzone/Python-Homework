# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:24:28 2019

@author: alf11
"""
class Account:
    def __init__(self, id, balance, annualInterestRate):
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
 
    def getMonthyInterestRate(self):
        return (annualInterestRate/12)/100
        
    def getMonthyInterest(self):
        return balance * getMonthyInterestRate(self)
 
acct_list =[Account(1, 100, 4.5), Account(2, 100, 4.5), Account(3, 100, 4.5),
            Account(4, 100, 4.5), Account(5, 100, 4.5), Account(6, 100, 4.5),
            Account(7, 100, 4.5), Account(8, 100, 4.5), Account(9, 100, 4.5),
            Account(10, 100, 4.5)]
 
 
def main():
        menu = 0
        while menu != 5:
            acct = eval(input("Enter an account number:"))
            if acct > 10:
                acct = eval(input("Please Enter a valid account number:"))
            acct = acct_list[acct-1]        
            while menu != 4:
                menu = eval(input("""Main Menu:
                                1: Check Balance
                                2: Withdraw
                                3: Deposit
                                4: Exit
                     
                                Enter a choice:"""))    
                if menu == 4:
                    break;
                elif menu == 1:
                    print ("The balance is: ", acct.getBalance())
                elif menu == 2:
                    withd = eval(input("Enter an amount to withdraw: "))
                    acct.setWithdraw(withd)
                elif menu == 3:
                    dep = eval(input("Enter an amount to deposit: "))
                    acct.setDeposit(dep)   
main()    
