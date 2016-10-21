def factorial(myNumber):   #function to calculate factorial of a number
    workingValue = 1
    while myNumber >= 1:
        workingValue = workingValue * myNumber
        myNumber = myNumber - 1
    print("Your factorial is " + str(workingValue))
    trailing(workingValue)



def trailing(factorialResult):    #function to count trailing 0's in factorial number
    count = 0
    index = -1
    factorialResult = str(factorialResult)
    for c in factorialResult:
        number = factorialResult[index]
        if int(number) == 0:
            count = count + 1
            index = index -1
        else:
            break
    print ("Number of trailing 0's is " + str(count))


    
originalNumber = int(input("Enter a number "))  #asks the user for the number to work on
num = factorial(originalNumber) #call to the factorial function with a parameter
