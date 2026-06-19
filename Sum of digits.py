num = int(input("Enter a number: "))
digit = 0
sum = 0
while(num>0):
    digit = num %10
    sum += digit
    num = num // 10
print(sum)
