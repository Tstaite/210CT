
x = []

number = int(input("Enter how many elements you want: "))
print ("Enter numbers in array: ")
for i in range (number):
    n = int(input("num :"))
    x.append(n)
print(x)


for Element in range (0,len(x)):
    if x[Element] == 5:
        x[Element] = 2
    elif x[Element] == 3:
        x[Element] = 8
    elif x[Element] == 8:
        x[Element] = 3
    elif x[Element] == 6:
        x[Element] = 1
    elif x[Element] == 1:
        x[Element] = 9
    elif x[Element] == 9:
        x[Element] = 7
    elif x[Element] == 2:
        x[Element] = 5
    elif x[Element] == 7:
        x[Element] = 6
print(x)
