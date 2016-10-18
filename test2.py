import random #imports the shuffle function only

def listCreation(x):   #function for list creation
    myList = [] 
    i=0 
    while i < listQuantity: 
        listItem = int(input("Enter list item "))
        myList.append(listItem)
        i=i+1
    print("Your selected list: " + str(myList))
    Shuffler(myList)   #call to second function
    
def Shuffler(theList): #function to shuffle created list
    list_length = len(theList)
    newList = []
    
    for i in range(list_length):
        a = random.choice(theList)
        newList.append(a)
        theList.remove(a)
        
    print(newList)


listQuantity = int(input("Enter the number of elements in the list "))
listCreation(listQuantity)    #Call to listCreation function

