def Perfect_Square(Mynumber):
    Integer = 1
    Answer = Integer*Integer

    while (Answer <= Mynumber):
        Integer = Integer + 1
        Answer = Integer * Integer

    Integer = Integer - 1
    Integer = Integer**2
    print("The highest perfect square before your number is " + str(Integer))



myNumber = int(input("Enter a number "))
Perfect_Square(myNumber)

