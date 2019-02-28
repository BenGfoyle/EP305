# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:01:42 2019

@author: Ben Guilfoyle - 16306203 - https://github.com/BenGfoyle/EP305

Overview: This program takes in a posative integer n, it will calculate the sum
of n, exp(n), n facotrial, and log base e of n facotrial for values 1 - n.
"""

import numpy as np #gives access to mathematical functions

def informUser():
    print("This program will request a posative integer 'N' as input.",\
          "The sum of N, e^N, N!, and ln(N!), for values 1 to N")

#newInput function to handle input, especially in the result of bas user input
def newInput():
    num = input("Please enter an integer between zero and twenty: ")
    try: #attempt to parse num to int
        num = int(num)
        if num > 0 and num < 21:
            return num
        else:
            print("You have entered an invalid value, try again please")
            newInput()
    except: #if error is thrown  eg letters entered
        print("You have entered an invalid value, try again please")
        newInput() #call newInput and try get a different input string

def sumOf(n): 
    total = 0
    for i in range(1,n+1): #iterate between 1 and n, get running total
        total = total + i
    return total

def expo(n): #call numpy to calcualte expontential
    n = np.exp(n)
    return n

def natural(n):
    try:
        n = np.log(n)
    except:
        n = "Cannot Compute!"
    return n

def factorial(n): 
    total = 1
    for i in range(1,n+1): #iterate between 1 and n, get running total
        total = total * i
    return total
   
def printHeadings():
    #headings for the table
    head1, head2, head3, head4,head5 = "N", "Sum of N", "e^N", "N!", "ln(N!)"
    print('{0:>8}'.format(head1), '{0:>10}'.format(head2),\
          '{0:>18}'.format(head3),'{0:>20}'.format(head4),\
          '{0:>10}'.format(head5))
    
def printing(num, sigma_N, exp_N, fact_N, nat_N):
    
    #parse some values to int as required
    fact_N = int(fact_N)
    nat_N = int(nat_N)
    
    print('{0:>8}'.format(num), '{0:>10.3f}'.format(sigma_N),\
          '{0:>18.3f}'.format(exp_N),'{0:>20}'.format(fact_N),\
          '{0:>10}'.format(nat_N))
    
def main():
    informUser()
    num = newInput()
    printHeadings()
    for i in range(1,num+1):
        sigma_N = sumOf(i)
        exp_N = expo(i)
        fact_N = factorial(i)
        nat_N = natural(fact_N)
        printing(i, sigma_N, exp_N, fact_N, nat_N)
        
if __name__ == "__main__": #go to main method
	main()