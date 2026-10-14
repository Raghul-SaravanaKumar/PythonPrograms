# Program Name: sum_of_array.py

def sum_of_array(arr):
  total = 0
  for num in arr:
    total += num
  return total


# Example Usage
numbers = [12, 45, 26, 6, 8, 33]
print("Sum of array elements:", sum_of_array(numbers))
