#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 09:27:49 2019

@author: BenGfoyle
@Overview: This program will write an array to a text file and output the
contents of the file to the screen
"""

#==============================================================================
def fileRead():
    """
    @Overview: This function reads the text file pendulum.txt and passes two
    lists back to the main method
    """

    #define lists and and file name
    fileName = "pendulum.txt"
    inFile = open(fileName,'r')
    sp_length = []
    sp_period = []


    header = inFile.readline()
    #get values from each line
    for line in inFile:
        values = line.split()
        sp_length.append(float(values[1]))
        sp_period.append(float(values[2]))

    #close file
    inFile.close()

    return sp_length, sp_period


#==============================================================================

#==============================================================================
def fileWrite(sp_length,sp_period):
    """
    @Overview: This function writes two arrays to the file pendulum.txt
    """

    #name and open file
    fileName = "pendulum.txt"
    outFile = open(fileName,'w')
    print("{0:>15}".format("Index"),\
          "{0:>15}".format("Length (cm)"),\
          "{0:>15}".format("Period (s)"), file = outFile)
    #print lsits to file
    for i in range(0, len(sp_length)):
        print("{0:>15}".format(i),\
              "{0:>15}".format(sp_length[i]),\
              "{0:>15}".format(sp_period[i]), file = outFile)

    #close file
    outFile.close()
#==============================================================================

#==============================================================================
def printData(sp_length,sp_period):
    """
    @Overview: This function prints to the screen the two arrays and index
    """
    #print heading
    print("{0:>15}".format("Index"),\
          "{0:>15}".format("Length (cm)"),\
          "{0:>15}".format("Period (s)"))

    #print lsits to file
    for i in range(0, len(sp_length)):
        print("{0:>15}".format(i),\
              "{0:>15}".format(sp_length[i]),\
              "{0:>15}".format(sp_period[i]))
#==============================================================================

#==============================================================================
def getData():
    """
    @Overview: This function reads the keyboard for user input for the arrays
    and returns both lists to the main method
    """
    #define n and lists
    sp_length = []
    sp_period = []
    c_length = 0.0
    c_period = 0.0
    #retrieve data from user input
    print("Please enter a non numeric value to when you are finished")
    i = 1
    while(type(c_length) == float and type(c_period) == float ):
        print("\nPlease enter a value for length ['",i,"']\n")
        c_length = input()

        #try parse to float
        try:
            c_length = float(c_length)


            print("Please enter a value for period ['",i,"']\n")
            c_period = input()
            c_period = float(c_period)

            sp_period.append(c_period)
            sp_length.append(c_length)
            i += 1
        #if user enters a non numeric character finish input
        except:
            print("Thank you, your data is being processed.")

    return sp_length, sp_period
#==============================================================================

#==============================================================================
def main():
    print("This program reads in user input, and writes it to a file.",\
    "The orignal data and the data read form the file is retireved and output")

    #get user defined data
    man_length, man_period = getData()

    #write user data to file
    fileWrite(man_length, man_period)

    #read the file
    file_length, file_period = fileRead()

    #print the data check they are the same
    print("\nData from manual entry\n")
    printData(man_length, man_period)
    print("\nData retrieved form file\n")
    printData(file_length, file_period)
#==============================================================================

main()
