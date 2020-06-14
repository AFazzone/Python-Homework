# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:38:39 2019

@author: alf11
"""

##  using the dickens .txt

def main():
    # Prompt the user to enter filenames
    f1 = input("Enter a filename: ").strip()
    old = input("Enter the old string to be replaced:")
    new = input("Enter a new string to replace the old:")

    # Open files for input 
    infile = open(f1, "r")
        
    s = infile.read() # Read all from the file 
    s = s.replace(old, new)
    
    outfile = open(f1, "w")
    print(s, file = outfile)
    outfile.close()
    
    print("Done")
    
    infile.close() # Close the output file

main()  