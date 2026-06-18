num = int (input("Enter a number: "))   
rev = 0 
og = num
while(num>0):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reverse of the number is: ",rev)
if(og == rev):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
