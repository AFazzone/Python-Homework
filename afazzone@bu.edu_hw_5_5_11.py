# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 13:58:11 2019

@author: alf11
"""

#score_list = []
#students, score_list = eval(input"Enter )

# Prompt the user to enter the number of students
numOfStudents = eval(input("Enter the number of students: "))

student1 = input("Enter a student name: ")
score1 = eval(input("Enter a student score: "))
max_student = student1
max = score1  
max2 = 0
max2_student = ""

for i in range(numOfStudents - 1):
    student = input("Enter a student name: ")
    score = eval(input("Enter a student score: ")) 
    if score > max:        
        max2 = max
        max2_student = max_student
        max = score
        max_student = student
    else: 
        if max > score > max2:
            max2 = score
            max2_student = student
        

            
print("Top student ", max_student, "'s score is ", max, "2nd best is",
      max2_student, "'s score is ", max2)