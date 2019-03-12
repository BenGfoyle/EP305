#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:19:21 2019

@author: BenGfoyle

Overview: This program will take in 2 values which correspond to the wavelength
of a photon of light in nanometers. The corresponding frequency, and energy in 
electron volts will be calculated. The output follows a predefined format.
"""
#import scipy to retieve constants
from scipy import constants as con

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
    prompt = 'Please enter a value for wavelength in nanometers',\
             'such that: 0 <= wavelength <=360'
    wave_l =input(prompt)
    try: #attempt to parse values to a float
        if wave_l > 360 or wave_l < 0:
            print("You entered a value outside the defined range, try again!")
            return newInput()

        #confirm user input is correct
        print("\nYou have entered:",wave_l)
        
        ans = input("\nIs this correct? [y/n]\n")
        if(ans == 'y'): 
            return wave_l
        else:
            print("You have selected no.")
            return newInput()
    except: #bad values or an inforseen error occured
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
    if wave_l == 0:
        energy = "UNDEFINED"
    else:
        energy = (LIGHT * PLANCK) / wave_l
    return energy()
#==============================================================================

#==============================================================================
def printing(energy,wavelength,head1,head2,head3):
    print("{g:.5e}".format((head1)),\
          "{g:.5e}".format((head2)),\
          "{g:.5e}".format((head3)))
    
#==============================================================================

#==============================================================================
def main():
    energy = []
    wave = []
    freq = []
    a = newInput()
    b = newInput()
    step = 30
    
    if b < a: #account for b less than a
        step = step *-1
        
    for i in range(a,b,step):
        #get energy and frequency
        currentEnergy = getEnergy(i)
        currentFrequency = getFreq(currentEnergy)
        
        #append calcualted values to relivent lists
        wave.append(i)
        energy.append(currentEnergy)
        freq.append(currentFrequency)

    printing(energy,wave,freq,"Energy eV","Wavelength (nm)","Frequency(Hz)")
        
#==============================================================================

if __name__ == "__main__":
    #inform user and go to main method
    informUser()
    main()