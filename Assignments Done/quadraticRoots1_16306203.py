# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:42:56 2019

@author: Ben Guilfoyle - https://github.com/BenGfoyle - 16306203

Overview: This program calculates the roots of quadratic functions.
"""

from numpy import sqrt #square root
from numpy import absolute as abs #absolute value

#-----------------------------------------------------------------------------#
def informUser():
    print("This program will calculate the roots of quadratic equations",\
          "of the form Ax^2 + Bx + C = 0\n")
#-----------------------------------------------------------------------------#
    
#-----------------------------------------------------------------------------#
def newInput():
    quad = input("Please enter A, B, and C seperated by commas Eg: 1.2,-5,2 :")
    quad = quad.split(',')
    try: #attempt to parse values to a float
        for i in range(0,len(quad)):
            quad[i] = float(quad[i])
            
        if quad[0] == 0:
            print(quad[0],"x\xb2","implies this is not a quadratic, try again")
            return newInput()

        #confirm user input is correct
        print("\nYou have entered:",quad[0],"x\xb2 +",quad[1], "x +" ,\
                    quad[2],"= 0.")
        
        ans = input("\nIs this correct? [y/n]\n")
        if(ans == 'y'): 
            return quad
        else:
            print("You have selected no.")
            return newInput()
            
    except ValueError: #deals with bad input eg letters
        print("\aYou seem to have entered an invalid value! Please try again.")
        return newInput() #call newInput and try get a different input string
    
    except IndexError: #if user enters less variables than required
        print("\aYou have not entered enough variables! Please try again.")
        return newInput() #call newInput and try get a different input string
    
    except: #something else went wrong entirelt       
        print("\Something went wrong, and we're not sure why please try again")
        return newInput()
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#    
def retry(): #reprompt user to ente ranother equation
    ans = input("Would you like to try another equation? [y/n]")
    if ans == 'y':
        print("You have entered yes!\n")
        main()
    else:
        print("Thank you shutting down...")
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#use minus b formula to calculate first root
def root1(a,b,c):
    maybeComplex = (b**2) - (4 * a * c)
    rootRe = -b/(2 * a)
    if maybeComplex < 0:
        maybeComplex = abs(maybeComplex) #possible complex component
        rootRe = -b/(2 * a)
        rootIm = -1*(sqrt(maybeComplex)) / (2 * a)  
        root = complex(rootRe,rootIm) #concatinate real and imaginary component
    else:
        root = rootRe - maybeComplex
    root = "{:.3e}".format(root)
    return root
#-----------------------------------------------------------------------------#
    
#-----------------------------------------------------------------------------#
#use minus b formula to calculate second root
def root2(a,b,c):
    maybeComplex = (b**2) - (4 * a * c) 
    rootRe = -b/(2 * a) 
    if maybeComplex < 0:
        maybeComplex = abs(maybeComplex) #possible complex component
        rootRe = -b/(2 * a)
        rootIm = -1*(sqrt(maybeComplex)) / (2 * a)  
        root = complex(rootRe,rootIm) #concatinate real and imaginary component
    else:
        root = rootRe + maybeComplex
    root = "{:.3e}".format(root)
    return root
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
def main():
    quad = newInput() #get user input
    #get roots
    root_1 = root1(quad[0],quad[1],quad[2])
    root_2 = root2(quad[0],quad[1],quad[2])
    
    #output to user
    print("The roots of ",quad[0],"x\xb2 +",quad[1], "x +",quad[2],"= 0 are:",\
          root_1,"and",root_2) 
    retry()
#-----------------------------------------------------------------------------#

if __name__ == "__main__": #go to main method
    informUser()
    main()
