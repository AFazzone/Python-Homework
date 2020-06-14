# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 17:31:02 2019

@author: alf11
"""



import random

x_list = [random.randint(0,9) for i in range(1000)]

print (x_list)

count0 = count1 = count2 = count3 = count4 = count5 = 0
count6 = count7 = count8 = count9 = 0

for e in x_list:          
    if e == 0:
        count0 +=1
    elif e == 1:      
        count1 +=1
    elif e == 2:      
        count2 +=1   
    elif e == 3:     
        count3 +=1
    elif e == 4:
        count4 +=1    
    elif e == 5:
        count5 +=1
    elif e == 6:
        count6 +=1   
    elif e == 7:
        count7 +=1
    elif e == 8:
        count8 +=1    
    else : 
        count9 +=1
            
print ("Zero occurs ", count0, " times,",
       "one occurs ", count1, " times,",
       "two occurs ", count2, " times,",
       "three occurs ", count3, " times,",
       "four occurs ", count4, " times,",
       "five occurs ", count5, " times,",
       "six occurs ", count6, " times,",
       "seven occurs ", count7, " times,",
       "eight occurs ", count8, " times,",
       "nine occurs ", count9, " times,",
       )


