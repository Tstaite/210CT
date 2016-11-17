from random import choice #import choice function only

def listCreation(x):   #function for list creation
    myList = [] 
    i=0 
    while i < listQuantity:  
        listItem = int(input("Enter list item ")) 
        myList.append(listItem) 
        i=i+1 
    print("Your selected list: " + str(myList))
    Shuffler(myList)   #call to shuffler function
    
def Shuffler(theList): #function to shuffle created list
    list_length = len(theList)
    newList = []
    
    for i in range(list_length):
        element = choice(theList) 
        newList.append(element) 
        theList.remove(element) 
        
    print(newList)


listQuantity = int(input("Enter the number of elements in the list "))
listCreation(listQuantity)  #Call to listCreation function

