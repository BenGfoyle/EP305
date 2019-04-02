# -*- coding: utf-8 -*-
# =============================================================================
# 
# Created on Tue Feb 19 13:49:40 2019
# 
# @author:Ben Guilfoyle - 16306203 - https://github.com/BenGfoyle/EP305
# 
#This program will take in a student mark from 0-100 and output their A-E grade
#It will continuously prompt the user to ent a grade until they enter a number
#Less than zero or greater than 100
# =============================================================================

def informUser(): #prints to the screen what the program does for the user
    print("This program will prompt you to enter a student mark (0-100),",\
          "the program will output the mark and its grade (A-E)")
    print("To quit the program enter a grad less than 0 or greater than 100")

#newInput function to handle input, especially in the result of bas user input
def newInput():
    num = input("Please enter the student mark (0-100): ")
    try: #attempt to parse mph to a float, and return mph 
        num = float(num)
        return num
    except ValueError: #if error is thrown (eg bad input such as letters)
        print("You seem to have entered an invalid value, note you do not",\
              " need to include the '%' symbol!")
        newInput() #call newInput and try get a different input string
        
#function to compare x against y and print relivent statements
def grades(mark):
    if mark >= 85:
        print("A mark of", mark , "equals an A-Grade")
    elif mark >=70:
        print("A mark of", mark , "equals an B-Grade")
    elif mark >=55:
        print("A mark of", mark , "equals an C-Grade")
    elif mark >=40:
        print("A mark of", mark , "equals an D-Grade")
    else:
        print("A mark of", mark , "equals an E-Grade")
  
def main():
    informUser()
    mark = newInput() #current mark equal t user input
    while(mark >= 0 and mark <= 100):  
        grades(mark)
        mark = newInput()
    print("Thank you, shutting down...")
        
if __name__ == "__main__": #go to main method
	main()

