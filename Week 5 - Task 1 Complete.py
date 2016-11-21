myList = [1,2,1,10,4,5,1,6,78,88,99]
myList2 = myList.copy() #copy of first list

FinalList = []

for element in myList:
    TempList = []
    for element in myList2:
        
        if len(TempList) == 0: #if temp list is empty append first item
            
            TempList.append(element)
        else:
            if element > TempList[-1]:
                TempList.append(element)
            else:
                myList2 = myList2[1:] #myList2 equals myList2 minus 1st element
                break
            if (len(TempList) > (len(FinalList))): #replace final list if temp list is greater
                FinalList = TempList
    
    
   
        
print(FinalList)


