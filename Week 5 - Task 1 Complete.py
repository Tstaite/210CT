myList = [1,2,1,3,4,5]
myList2 = myList.copy()

FinalList = []

for i in myList:
    TempList = []
    for i in myList2:
        
        if len(TempList) == 0:
            
            TempList.append(i)
        else:
            if i > TempList[-1]:
                TempList.append(i)
            else:
                myList2 = myList2[1:]
                break
            if (len(TempList) > (len(FinalList))):
                FinalList = TempList
    
    if (i == 5):
        myList2 = myList2[1:]
   
        
print(FinalList)


