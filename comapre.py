# -*- coding: utf-8 -*-

# =============================================================================
# Created on Tue Feb 19 13:10:54 2019
#Lab Session 3 Question 1
# @author: guilf
# This program takes in two integers, and outputs which is greater, and if they 
# are equal
# 
# =============================================================================

def informUser():
    print("This program will prompt you to enter two integers (x and y)",\
          "x and wil be compared and a relational statement will be printed")

#newInput function to handle input, especially in the result of bas user input
def newInput():
    num = input("Please enter a posative integer: ")
    try: #attempt to parse mph to a float, and return mph 
        num = int(num)
        if num <= 0:#check num is negative
            print("You seem to have entered an invalid value, please enter",\
                        "a posative integer!")
            newInput() #reprompt the user for new input
        return num
    except ValueError: #if error is thrown (eg bad input such as letters)
        print("You seem to have entered an invalid value, please enter",\
                        "a posative integer!")
        newInput() #call newInput and try get a different input string
        
#function to compare x against y and print relivent statements
def compare(x,y):
    if x > y:
        print("x,", x , ",is greater than y,", y)
    elif x < y:
        print("x,", x , ",is less than y,", y)
    else:
        print("x,", x , ",is equal to y,", y)
  
def main():
    informUser()        
    x = newInput()
    y = newInput()
    compare(x,y)     
        
if __name__ == "__main__":
	main()