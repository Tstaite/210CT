def splitText(string): #function to split a string into seperate words
    
    myList = []
    words = string.split()
    for i in words: #append seperate words to a list
        myList.append(i)
    solution = Reverse(myList) #call reverse function
    print(solution)

def Reverse(MySentence):  #Fuinction to revrse order of a sentence
    if len(MySentence) == 0:
        return MySentence
    else:
        print(MySentence)
        return MySentence[-1] + " " + str(Reverse(MySentence[:-1])) #Adds the remaining elements in the list ot the last element.




data = input("Enter a string")
splitText(data) #call splitText function with user input



