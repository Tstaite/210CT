amount = list()
x = int(input("how many eggs per day?"))
y = int(input("how many days?"))

l = 0
i = 0
while i < y:
    amount.append(1)
    i = i+1

for j in amount:
        j = j*x
        l = l+j

print(str(l) + " eggs hatched")
