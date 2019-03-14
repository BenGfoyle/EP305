#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:46:53 2019

@author: BenGfoyle

Overview: This program numerically calculates the curve length of a semicirlcle
"""

import numpy as np #for pi
import matplotlib.pyplot as plt #for pltting graphs

#define constants and global variables
PI = np.pi
n = 1 #inital value to iterate over

all_n = []
n_length = []

#==============================================================================
def informUser():
    print("The program numerically calculates the curve length of a",\
          "semicircle of radius 1 unit length for two growth factors of n.\n")
#==============================================================================

#==============================================================================
def makeGraph(yAxis,xAxis,name):
    plt.scatter(xAxis,yAxis, label = name)
    plt.legend(name)
    plt.semilogx(xAxis,yAxis) #logarithmic x axis to help with visuals
    plt.xlabel("log n")
    plt.ylabel("length")
    plt.title("Plot of log n vs curve length")
    plt.legend(loc='lower right')
    plt.show()
#==============================================================================

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
#n is the number of subdivisions of the diameter of the semicircle
#prev_length is the value of the previous length segment, used to find error
# nGrowth is the factor at which n will grow by over the iterations
def main(n,prev_length,nGrowth):
    #radius = 1
    c_length = 0
    xmax = 1
    xmin = -1

    dx = (xmax - xmin)/n

    for i in range(0,n): #iteratre over distance to n
        x = xmin + i*dx #set new current x position
        c_length = c_length + newLength(x,dx) #incriment length by new length
        c_error = abs(prev_length - c_length) #find error base off known value

    printing(n, c_length, c_error)
    all_n.append(n)
    n_length.append(c_length)

    if c_error > 1e-6: #if error is not within acceptable value
        return main(n * nGrowth, c_length, nGrowth)#call main again with new n
#==============================================================================

if __name__ == "__main__":
    #inform user, and print headings and go to main method
    informUser()
    printing("n", "length", "error")
    main(n,0,2)
    print("\n")
    makeGraph(n_length,all_n,"n = 2 * n")
    #clear values in the lists for new data
    all_n.clear()
    n_length.clear()

    printing("n", "length", "error")
    main(n,0,10)
    print("\n")
    makeGraph(n_length,all_n, "n = n * 10")



    print("The asymptotic behaviour is much more apparent when n increases",\
          "by a factor of two rather than a factor of ten. This is due to",\
          "the step size being too large when probaing by factors of ten.")
