def remove_duplicates(arr):
  seen = set()
  result = []
  for item in arr:
    if item not in seen:
      seen.add(item)
      result.append(item)
  return result


# Example usage
arr = [4, 5, 9, 4, 2, 5, 8, 9]
print("Unique Array:", remove_duplicates(arr))
