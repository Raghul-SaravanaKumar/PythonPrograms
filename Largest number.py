n = int(input("Enter the Range of the List"))
elements = []
for i in range (n):
    element= int (input("enter the values"))
    elements.append(element)
elements.sort()
print(elements[len(elements)-1])
