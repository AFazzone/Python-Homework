# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 06:43:24 2019

@author: alf11
"""

x_str = """It was the best of times, it was the worst of times,
 it was the age of wisdom, it was the age of foolishness, it 
 was the epoch of belief, it was the epoch of incredulity, it
 was the season of Light, it was the season of Darkness, it 
 was the spring of hope, it was the winter of despair, 
 we had everything before us, we had nothing before us,
 we were all going direct to Heaven, we were all going 
 direct the other way – in short, the period was so far 
 like the present period, that some of its noisiest authorities
 insisted on its being received, for good or for evil,
 in the superlative degree of comparison only"""
 
 
# Remove the word "was" 
x_strip = x_str.strip()
x_len = len(x_strip)

y_str = x_str.replace("was", '')
print (y_str)
y_strip = y_str.strip()
y_len = len(y_strip)

count = (x_len - y_len) / 3
print ()
print ("""The word "was" has been removed""", count, "times.")
print ()
 
 
#Remove "was" using iteration
x_list = x_str.split(" ") 
y_list = []
was_list = ["was"]
count1 = x_list.count('was')

for word in x_list:
    if word not in was_list:
        y_list.append(word)
        
print (" ".join(y_list))
print ()
print ("""The word "was" has been removed""", count1, "times")
print ()


#Every 5th word backwards

x_list3 = x_str.split(" ")
y_list3 = [x[::-1] for x in x_list3]
 
x_list3[4::5] = y_list3[4::5]
 
print(" ".join(x_list3))

