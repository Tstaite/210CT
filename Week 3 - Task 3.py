def VowelRemove(i, string): #function to remove vowel from a string
    if string[i] in ("a", "e", "i", "o", "u"): #checks is element is a vowel
        i = i + 1
    else:
        newstring.append(string[i])
        i = i + 1
    
    if i >= len(string):
        finalString = ''.join(newstring)
        print (finalString)
    else:
        VowelRemove(i, string) #calls function again
        


 





string = input("Enter your string ")
i = 0
newstring = []
VowelRemove(i, string)
