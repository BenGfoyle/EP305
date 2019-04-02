#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:46:53 2019

@author: BenGfoyle
"""

import numpy as np

#define constants and global variables
PI = np.pi
n = 1

#==============================================================================
def f(x): #calulate f(x), ref equation of a circles
    y = np.sqrt(1 - x**2)
    return y
#==============================================================================

#==============================================================================
def newLength(x,dx):#calcualte new length based off pytagoras
    dist = np.sqrt((dx)**2 + (f(x) - f(x + dx))**2) 
    return dist
#==============================================================================

def printing(n,length, error): #pretty printing/formatting
    try:
        print('{0:>18}'.format(n), '|',\
              '{0:>18.7f}'.format(length), '|',\
              '{0:>18.7f}'.format(error), '|')
    except:
        print('{0:>18}'.format(n), '|',\
              '{0:>18}'.format(length), '|',\
              '{0:>18}'.format(error), '|')
    

#==============================================================================
def main(n):
    #radius = 1
    c_length = 0
    xmax = 1
    xmin = -1
    
    dx = (xmax - xmin)/n
    
    for i in range(0,n): #iteratre over distance to n
        x = xmin + i*dx #set new current x position
        c_length = c_length + newLength(x,dx) #incriment length by new length
        c_error = PI - c_length #find error base off known value
    
    printing(n, c_length, c_error)
    
    if c_error > 1e-6: #if error is not within acceptable value
        return main(n * 2)#call main again with n = n * 2
#==============================================================================
        
if __name__ == "__main__":
    #inform user and go to main method
    printing("n", "length", "error")
    main(n)