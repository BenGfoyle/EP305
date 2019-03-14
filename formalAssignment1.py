#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:19:21 2019

@author: BenGfoyle - 16306203 - github.com/bengfoyle/ep305

Overview: This program will take in 2 values which correspond to the wavelength
of a photon of light in nanometers. The corresponding frequency, and energy in 
electron volts will be calculated. The output follows a predefined format.
"""
#import scipy to retieve constants
from scipy import constants as con
from numpy import arange

#define constants
PI = con.pi
PLANCK = con.Planck
LIGHT = con.c
EV = con.eV

#==============================================================================
def informUser():
    print("This program will take in 2 values a and b which correspond to",\
          "the wavelength of a photon of light in nanometers. The ",\
          "corresponding frequency, and energy in electron volts will be",\
          "calculated between the values of a and b. The output follows",\
          "a predefined format.")
#==============================================================================

#==============================================================================
def newInput():
    prompt = "Enter a value for wavelength in nanometers:\n"
    wave_l =input(prompt)
    try: #attempt to parse values to a float
        wave_l = float(wave_l)
        return wave_l
        
    except ValueError: #bad values or an inforseen error occured
        print("You may have entered an invalid value please try again!")
        return newInput()
#==============================================================================

#==============================================================================
def getFreq(energy):
    if energy == "UNDEFINED":
        freq = "UNDEFINED"
    else:
        
        freq = energy / PLANCK
    return freq
#==============================================================================
    
#==============================================================================
def getEnergy(wave_l):
    if wave_l <= 0:
        energy = "UNDEFINED"
    else:
        energy = (LIGHT * PLANCK) / wave_l
    return energy
#==============================================================================

#==============================================================================
def printing(head1,head2,head3):
    try:
        print("{0:g>27.5e}".format((head1)),'\\',\
              "{0:g>27.5e}".format((head2)),'\\',\
              "{0:g>27.5e}".format((head3)))
    except:
        print("{0:g>27}".format((head1)),'\\',\
              "{0:g>27}".format((head2)),'\\',\
              "{0:g>27}".format((head3)))
    
#==============================================================================


#==============================================================================
def findMin(a,b):
    minimum = 0
    difference = a - b #posative if a > b, negative if b > a
    
    if difference > 0:
        bMin = b - minimum #posative if b > minimum negative if minimum > b
        if 0 > bMin:
            minimum = b
    
    else:
        aMin = a - minimum
        if 0 > aMin:
            minimum = a
    
    return minimum
    
#==============================================================================
        
#==============================================================================
def findMax(a,b):
    maximum = 360
    difference = a - b #posative if a > b, negative if b > a
    
    if difference < 0:
        bMax = b - maximum #posative if b > minimum negative if minimum > b
        if 0 < bMax:
            maximum = b
    
    else:
        aMax = a - maximum
        if 0 < aMax:
            maximum = a
    
    return maximum
    
#==============================================================================
        
#==============================================================================
def main():
    energy = []
    wave = []
    freq = []
    a = newInput()
    b = newInput()
    mini = findMin(a,b)
    print(mini)
    
    maxi = findMax(a,b)
    print(maxi)
    
    step = 30
    
    printing("Wavelength (nm)","Energy eV","Frequency(Hz)")
        
    for i in arange(mini,maxi,step):
        #get energy and frequency
        currentEnergy = getEnergy(i)
        currentFrequency = getFreq(currentEnergy)
        
        #append calcualted values to relivent lists
        wave.append(i)
        energy.append(currentEnergy)
        freq.append(currentFrequency)
        
    for i in range(0,len(energy)):
        printing(wave[i],energy[i],freq[i])
        
#==============================================================================

if __name__ == "__main__":
    #inform user and go to main method
    informUser()
    main()