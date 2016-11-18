#function to calculate factorial of a number
def factorial(myNumber):   
    myFactorial = 1
    while myNumber >= 1:
        myFactorial = myFactorial * myNumber
        myNumber = myNumber - 1
    print("Your factorial is " + str(myFactorial))
    trailing(myFactorial)


#function to count trailing 0's in factorial number
def trailing(factorialResult):    
    count = 0
    index = -1
    factorialResult = str(factorialResult)
    for element in factorialResult: 
        number = factorialResult[index] 
        if int(number) == 0: #if the last no. is 0, increment count
            count = count + 1
            index = index -1
        else:
            break
    print ("Number of trailing 0's is " + str(count))


    
originalNumber = int(input("Enter a number "))  #input number
num = factorial(originalNumber) #call to the factorial function with number
