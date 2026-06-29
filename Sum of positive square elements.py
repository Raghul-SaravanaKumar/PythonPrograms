n = int(input("Enter the size of the array: "))

print("Enter the elements of the array:")
sum_sq = 0

for i in range(n):
    x = int(input())
    if x > 0:
        sum_sq += x * x

print("Sum of positive square elements :", sum_sq)
