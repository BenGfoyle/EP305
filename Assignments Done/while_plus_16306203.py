# -*- coding: utf-8 -*-
# =============================================================================
# 
# Created on Tue Feb 19 13:49:40 2019
# 
# @author:Ben Guilfoyle - 16306203 - https://github.com/BenGfoyle/EP305
# 
#This program will prompt the user to enter a temperture between 0 and 100 C.
#The temperture will be converted to farenheit and print the conversion. 
#A description of the temperture will also be printed.
#Program will terminate if user enters value less than 0
# =============================================================================

def informUser(): #prints to the screen what the program does for the user
    print("This program will prompt you to enter a temperature in celcius,",\
          "the program will output the temperture in farenheit, and give a",\
          "description of the temperture")
    print("To quit the program enter a value less than 0.")

#newInput function to handle input, especially in the result of bas user input
def newInput():
    num = input("Please enter a temperature in celcius (0-100): ")
    try: #attempt to parse mph to a float, and return mph 
        num = float(num)
        return num
    except ValueError: #if error is thrown (eg bad input such as letters)
        print("You seem to have entered an invalid value, note you do not",\
              " need to include the 'C°' symbol!")
        newInput() #call newInput and try get a different input string
        
#this function converts from celcius tempC to farenheit tempF
def convert(tempC):
    #round to 2 places
    tempF = (9/5) * tempC +32  #conversion factor 
    tempC = round(tempC,2)
    tempF = round(tempF,2)
    print(tempC, "degrees centigrade =", tempF , "degrees Fahrenheit.")
    return tempF

#Colour changer for different outputs
def colourText(text,colour):
        CRED = '\033[31m'
        CBLUE = '\033[34m'
        CGREEN = '\033[32m'
        CEND = '\033[0m'
        
        if colour == "red":
            return CRED + text + CEND
        elif colour == "blue":
            return CBLUE + text + CEND
        elif colour == "green":
            return CGREEN + text + CEND
 
#function to compare x against y and print relivent statements
def compare(tempC,tempF):
    if tempC > 32 :
        desciption = "The temperature is rather warm"
        print(colourText(desciption,"red"))
    elif tempF <= 59:
        desciption = "The temperature is quite cool."
        print(colourText(desciption,"blue"))
    else:
        desciption = "The temperature is comfortable"
        print(colourText(desciption,"green"))
    
  
def main():
    informUser()
    tempC = newInput() #current mark equal t user input
    while(tempC >= 0):  #while temp greater than zero
        tempF = convert(tempC)
        compare(tempC,tempF)
        tempC = newInput()
    print("Thank you, shutting down...")
        
if __name__ == "__main__": #go to main method
	main()