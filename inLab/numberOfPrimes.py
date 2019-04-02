#count primes between bound 1 and 2
bound1 = 1 
bound2 = 100000
count = 0 #Keep track of number of prime

for i in range(bound2,bound1-1,-1):
    isPrime = True
    if i == 1 :
        isPrime = False
    else:
        if i%2 != 0 or i == 2: #if number is odd check if its prime, all even numbers are non prime
            for j in range(int(i/2),bound1-1,-1):
                if i%j == 0 and j != 1:
                    isPrime = False
                    break
            if isPrime == True:
                count = count + 1
                #print(i)
print("Number of Primes between,",bound1,"and",bound2,"=",count)
            
    
