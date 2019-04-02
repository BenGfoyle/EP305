# =============================================================================
# Created on Tue Feb 12 2019
# 
# Ben Guilfoyle - 16306203 - https://github.com/BenGfoyle/EP305
#
# NOTE: It is a bit hard to see the length 25 right justification as with 5
# decimals of precision the output string is over 25 characters in length,
# this diminishes the effect of the 25 character right justification.
# By editing degrees of precision in RightFormat function the justification 
# can be made more visible, or by changing the right jsutification form 25 to 
# a larger value eg:40
# 
# Overview;
# This program takes in a value in miles per hour.
# The value is then returned in meters per second.
# The output is formatted in 2 different styles;
# 20 spaces wide, with 3 decimals of precision, left justified
# 25 spaces wide, with 5 decimals of precision, right justified
# =============================================================================

# =============================================================================
# constant factor that allows the conversion from mile/hour to meters/second
# 1609.34 represents the conversion from miles to meter
# 3600 represents the conversion from hour to second
# =============================================================================

CON_FACTOR = float(1609.34/3600) 

# =============================================================================
# @param ms float
# This function takes in one float, ms (meters per second).
# This is then rounded to 3 decimal places using round() function
# It is printed, left justified to 25 places using the format() function
# =============================================================================

def LeftFormat(ms,mph):
    msRound = str(round(ms, 3))
    mphRound = str(round(mph,3))
    output = "Meters/Second:" + msRound + ", Miles/Hour:" + mphRound
    print('{0:<20}'.format(output))

# =============================================================================
# @param ms float
# This function takes in one float, ms (meters per second).
# This is then rounded to 5 decimal places using round() function
# It is printed, right justified to 20 places using the format() function
# =============================================================================

def RightFormat(ms,mph):
    msRound = "{:.5e}".format((ms))
    mphRound = "{:.5e}".format((mph))
    output = "Meters/Second:" + msRound + ", Miles/Hour:" + mphRound
    print("{0:>25}".format(output))
    
#newInput function to handle input, especially in the result of bas user input
def newInput():
    mph = input("Please enter a velocity in miles per hour: ")
    try: #attempt to parse mph to a float, and return mph 
        return float(mph)
    except ValueError: #if error is thrown (eg bad input such as letters)
        print("You seem to have entered an invalid value, please enter",\
                        "a number!")
        newInput() #call newInput and try get a different input string
            
mph = newInput() #function call to retrieve input  
ms = mph * CON_FACTOR #arithmatic to convert to meters per second

# The print give s a title for the operation being done
print("\nMiles per Hour(mph) to Meters per Second Conversion(ms), in 2 Styles")

# =============================================================================
# There are 2 function calls here.
# As described above these functions will format the mph to ms conversion
# =============================================================================

LeftFormat(ms,mph)
RightFormat(ms,mph)
