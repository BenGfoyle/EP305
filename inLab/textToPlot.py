#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 09:27:49 2019

@author: BenGfoyle
@Overview: This program will write an array to a text file and output the
contents of the file to the screen
"""

import numpy as np #for pi
import matplotlib.pyplot as plt #for ploting graphs

#==============================================================================
def makeGraph(xAxis,yAxis,xName,yName,namePlot,title):
    plt.plot(xAxis,yAxis, label = namePlot, color = "red") #scatter plot
    plt.scatter(xAxis,yAxis, label = namePlot, color = "blue") #line plot
    #plt.bar(xAxis,yAxis, label = namePlot) #bar plot
    plt.legend(namePlot)
    plt.legend(loc='lower right')
    plt.xlabel(xName)
    plt.ylabel(yName)
    plt.title(title)
    plt.grid()
    plt.show()
#==============================================================================

#==============================================================================
def fileRead(file,delim):
    """
    @Overview: This function reads the text file and passes two
    lists back to the main method
    """

    #define lists and and file name
    fileName = file
    inFile = open(fileName,'r')
    ax1 = []
    ax2 = []


    header = inFile.readline()
    #get values from each line
    for line in inFile:
        values = line.split(delim)
        ax1.append(float(values[0]))
        ax2.append(float(values[1]))

    #close file
    inFile.close()

    return ax1,ax2
#==============================================================================

#==============================================================================
def fileWrite(ax1,ax2,file):
    """
    @Overview: This function writes two arrays to the file pendulum.txt
    """

    #name and open file
    fileName = file
    outFile = open(fileName,'w')
    print("{0:>15}".format("Index"),\
          "{0:>15}".format("Ax1"),\
          "{0:>15}".format("Ax2"), file = outFile)
    #print lsits to file
    for i in range(0, len(ax1)):
        print("{0:>15}".format(i),\
              "{0:>15}".format(ax1[i]),\
              "{0:>15}".format(ax2[i]), file = outFile)

    #close file
    outFile.close()
#==============================================================================

#==============================================================================
def printData(ax1,ax2):
    """
    @Overview: This function prints to the screen the two arrays and index
    """
    #print heading
    print("{0:>15}".format("Index"),\
          "{0:>15}".format("Ax1"),\
          "{0:>15}".format("Ax2"))

    #print lsits to file
    for i in range(0, len(ax1)):
        print("{0:>15}".format(i),\
              "{0:>15}".format(ax1[i]),\
              "{0:>15}".format(ax2[i]))
#==============================================================================

#==============================================================================
#read the file
file = input("Please enter the file name, include type (file1.txt)")
delim = " "
ext = file[len(file) - 3 : len(file)]
delim = input("Enter the delimiter character")

try:
    ax1,ax2 = fileRead(file,delim)
    #print the data check they are the same
    print("\nData from file\n")
    printData(ax1,ax2)
    makeGraph(ax1,ax2,"Axis 1","Axis 2","f(x)","Plot of Axis1 vs Axis 2")

except:
    print("You may have entered an invalid file name, or delimiter character")
#==============================================================================
