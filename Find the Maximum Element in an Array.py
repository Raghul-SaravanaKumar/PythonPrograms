# Program Name: find_maximum.py

def find_maximum(arr):
  if not arr:
    return None
  max_val = arr[0]
  for num in arr:
    if num > max_val:
      max_val = num
  return max_val


# Example Usage
numbers = [12, 45, 26, 6, 8, 33] [0.1.4]
print("Maximum element:", find_maximum(numbers))
