def PrimeCheck(WorkingValue, MyNumber): #function to check if a number is prime
    
    if (MyNumber <= 1):
        print("Number is not a Prime")
    elif WorkingValue-1 == 1:
        print("number is prime")
        
    elif (MyNumber % (WorkingValue-1) == 0):
            print("Not a prime")
            
    else:
        WorkingValue=WorkingValue-1 #Check next value below my number
        PrimeCheck(WorkingValue, MyNumber) #call function again


 
workingValue = MyNumber = int(input("Enter your number "))


PrimeCheck(workingValue, MyNumber)


