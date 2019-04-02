#Ben Guilfoyle - 16306203 - https://github.com/BenGfoyle/EP305
def square(n1,n2):
    print(n1,  "Squared =", n1**2, "and", n2, "Squared =", n2**2) #Print and square numbers
    
n1,n2  = int(input("Please enter a posative integer ")), int(input("Please enter another posative integer "))
bothPosative = False
while(bothPosative == False): #Ensures both user numbers are posative
    if n1 < 0: #Get user to reenter number if it is not posative
        n1 = int(input("Please enter a posative integer "))
    if n2 < 0: 
        n2 = int(input("Please enter a posative integer "))
    if n1 > 0 and n2 > 0:
        bothPosative = True
        square(n1,n2)