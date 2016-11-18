#function to calculate the highest perfect square
def Perfect_Square(Mynumber):
    
    #check datatype of input
    try: 
        Mynumber = int(Mynumber)
    except ValueError:
        print("Incorrect datatype")
        return
    
    Integer = 1
    Answer = Integer*Integer
    if (Mynumber == 1):
         print("The highest perfect square before your number is " + str(Integer))
    elif (Mynumber < 1):
        print("number must be greater than 0")
    else:
        #multiply each number by itself and see if the result is bigger
        while (Answer <= Mynumber):
            Integer = Integer + 1
            Answer = Integer **2 

        Integer = Integer - 1 
        Integer = Integer**2
        print("The highest perfect square before your number is " + str(Integer))



myNumber = input("Enter a number ")
Perfect_Square(myNumber)

