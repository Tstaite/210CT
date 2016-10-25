def Reverse(MySentence):  #Fuinction to revrse order of a sentence
    if len(MySentence) == 0:
        return MySentence
    else:
        print(MySentence)
        return MySentence[-1] + " " + str(Reverse(MySentence[:-1])) #Adds the remaining elements in the list ot the last element.


data = "This", "is", "my", "data"


Solution = (Reverse(data))
print(Solution)


