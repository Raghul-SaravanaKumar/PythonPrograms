# Program Name: search_element.py

def search_element(arr, target):
  for num in arr:
    if num == target:
      return True
  return False


# Example Usage
numbers = [12, 45, 26, 6, 8, 33]
target_val = 26
found = search_element(numbers, target_val)
print(f"Element {target_val} exists in array: {found}")
