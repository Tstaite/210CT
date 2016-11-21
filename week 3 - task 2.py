def PrimeCheck(workingValue, myNumber): #function to check if a number is prime
     #check datatype of input
   
    
    if (myNumber <= 1):
        print("Number is not a Prime")
    elif workingValue-1 == 1:
        print("number is prime")
        
    elif (myNumber % (workingValue-1) == 0):
            print("Not a prime")
            
    else:
        workingValue=workingValue-1 #Check next value below my number
        PrimeCheck(workingValue, myNumber) #call function again


 
workingValue = myNumber = int(input("Enter your number ")) #assign two variables to one value


PrimeCheck(workingValue, myNumber) #initial call to function


