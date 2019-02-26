# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:01:42 2019

@author: Ben Guilfoyle - 16306203 - https://github.com/BenGfoyle/EP305

Overview: This program will output sin and cos of 12 values at equal intervals
between 0 and 2pi (0 and 360 degrees). A table will be output featuring the 
angle in radians, degrees, and the sin and cos of the angle. 
"""
import numpy as np #gives access to trig functions

PI = np.pi #3.14159...

#12 equal values 0-360 degrees in a list
DEG_LIST = [0,30,60,90,120,150,180,210,240,270,300,330,360] 

rad_list = [] #empty list, will be used to store radian conversion of DEG_LIST
sin_list = [] #empty list, will be used to store sin conversion of rad_list
cos_list = [] #empty list, will be used to store cos conversion of rad_list

def degToRad(degrees): #function to convert degrees to radian
    RAD_CON = PI/180 #factor to convert from degrees to radians
    rad = RAD_CON * degrees
    return rad
 
def printing(deg, rad, sin, cos):
    #infor the user of what the program does
    print("This program will output the sin and cos of an 12 angles at equal",\
          "intervals between zero and 2 pi")
    
    #headings for the table
    head1, head2, head3, head4 = "X (Degrees)","X(Radians)","Sin(X)","Cos(X)"
    print('{0:>8}'.format(head1), '{0:>12}'.format(head2),\
          '{0:>16}'.format(head3),'{0:>16}'.format(head4))
    
    #loop to print the output
    for i in range(0,len(deg)): #iterate over deg list
        print('{0:>8.3f}'.format(deg[i],3), '{0:>12.3f}'.format(rad[i]),\
              '{0:>16.3f}'.format(sin[i]),'{0:>16.3f}'.format(cos[i]))
    
    
    

for i in range(0,len(DEG_LIST)): #loop over all elements in DEG_LIST
    rad = degToRad(DEG_LIST[i]) #call degToRad function on current list element
    rad_list.append(rad) #append rad to end of rad_list
    
    sinAngle = np.sin(rad) #calculate sin of angle using numpy
    sin_list.append(sinAngle) #append sinAngle to end of sin_list
    
    cosAngle = np.cos(rad) #calculate cos of angle using numpy
    cos_list.append(cosAngle) #append cosAngle to end of cos_list

printing(DEG_LIST, rad_list, sin_list, cos_list)
    


