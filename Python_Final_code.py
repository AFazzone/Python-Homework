# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 07:25:00 2019

@author: alf11
"""

import random
 
words = ["python", "apple", "computer", "science"]
 
gallows = """  
_________
|       |
|       
|    
|    
|    
|______   """ 
 
head_pic = """  
_________
|       |
|       0
|         
|    
|    
|______   """ 
    
torso_pic = """  
_________
|       |
|       0
|       |  
|       |
|    
|    
|______   """ 
 
 
r_leg_pic = """  
_________
|       |
|       0
|       |  
|       |
|        \
|    
|______   """ 
 
 
l_leg_pic = """  
_________
|       |
|       0
|       | 
|       |
|      / \
|    
|______   """ 
 
r_arm_pic = """  
_________
|       |
|       0
|       |/ 
|       |
|      / \
|    
|______   """ 
 
l_arm_pic = """  
_________
|       |
|       0
|      \|/ 
|       |
|      / \
|    
|______   """ 
    
    
game_word = random.choice(words)   # Choose a random word from the list for the game
 
game_letters = list(game_word)  #Break apart the word into letters
 
mystery = ["-" for e in range(len(game_word))]     #Replace all of the letters in the word with blanks
 
class hangMan():
    def __init__ (self, head, torso, r_leg, l_leg, r_arm, l_arm):
        self.__head = head
        self.__torso = torso
        self.__r_leg = r_leg
        self.__l_leg = l_leg
        self.__r_arm = r_arm
        self.__l_arm = l_arm
        
    def getPicture(self):
        if self.__l_arm == 1:
            print(l_arm_pic)
        elif self.__r_arm == 1:
            print(r_arm_pic)
        elif self.__l_leg == 1:
            print(l_leg_pic)
        elif self.__r_leg == 1:
            print(r_leg_pic)
        elif self.__torso == 1:
            print(torso_pic)
        elif self.__head == 1:
            print(head_pic)
    
#Create 7 instances of hangmen, 1 stands for for positive appendages
 
hang = [hangMan(0,0,0,0,0,0), hangMan(1,0,0,0,0,0), hangMan(1,1,0,0,0,0),
        hangMan(1,1,1,0,0,0), hangMan(1,1,1,1,0,0), hangMan(1,1,1,1,1,0),
        hangMan(1,1,1,1,1,1)]
 
#Wrong guess function displays the appropriate hangman picture
def wrong(wrong_guess, hang_pos):
        if wrong_guess == 6:
            print()
            print("You lose.")
            print (hangMan.getPicture(hang[hang_pos]))    
        else:
            print()
            print("You have chosen poorly")
            print (hangMan.getPicture(hang[hang_pos]))
    
menu = {1: "Play Again", 2: "Exit"}

        
def main():              
    print(gallows)
    wrong_guess = 0
    hang_pos = 0
 
    while wrong_guess < 6:
        print (mystery)  
        letter_choice = input("Guess a letter: ")
        if letter_choice in game_letters:
            pos = [i for i in range(len(game_letters)) 
                    if game_letters[i] == letter_choice]
            for e in range(len(pos)):
                mystery[pos[e]] = letter_choice
            if "-" not in mystery:
                print("YOU WIN!")
                print (mystery)
                break;
            else:
                print()
                print("Good Choice!")
        else:
            wrong_guess +=1
            hang_pos +=1
            wrong(wrong_guess, hang_pos)
        
    for i in menu:
        print (i, menu[i])
    restart = eval(input("Enter a number: "))
    if restart == 1:
        main()
    else:
        print("Thanks for playing!")
        
    
main()
 