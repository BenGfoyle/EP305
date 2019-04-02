#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:46:53 2019

@author: BenGfoyle
"""

import numpy as np

#define constant pi
PI = np.pi

#==============================================================================
def f(x):
    y = np.sqrt(1 - x**2)
    return y
#==============================================================================

#==============================================================================
def newLength(x,dx):    
    dist = np.sqrt((dx)**2 + (f(x) - f(x + dx))**2)
    return dist
#==============================================================================

def printing(n,length, error):
    try:
        print('{0:>18}'.format(n), '|',\
              '{0:>18.7f}'.format(length), '|',\
              '{0:>18.7f}'.format(error), '|')
    except:
        print('{0:>18}'.format(n), '|',\
              '{0:>18}'.format(length), '|',\
              '{0:>18}'.format(error), '|')
    

#==============================================================================
def main():
    #radius = 1
    c_length = 0
    xmax = 1
    xmin = -1
    n = 1
    
    c_error = 0
    
    printing("n", "length", "error")
    
    while(True):
        dx = (xmax - xmin)/n
        for i in range(0,n):
            x = xmin + i*dx
            c_length = c_length + newLength(x,dx)
            c_error = PI - c_length
        
        printing(n, c_length, c_error)
        if(c_error > 1e-6):
            n = n * 2
        else:
            break
        
#==============================================================================
if __name__ == "__main__":
    #inform user and go to main method
    main()
    

