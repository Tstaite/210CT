def VowelRemove(element, string): #function to remove vowels from a string
    if string[element] in ("a", "e", "i", "o", "u"): #checks if element is a vowel
        element = element + 1 #if so, skip element
    else:
        newstring.append(string[element])
        element = element + 1
    
    if element >= len(string): #if all elements checked...
        finalString = ''.join(newstring) #...join elements and print
        print (finalString)
    else:
        VowelRemove(element, string) #calls function again
        


 





string = input("Enter your string ")
element = 0
newstring = []
VowelRemove(element, string) #initial call to function
