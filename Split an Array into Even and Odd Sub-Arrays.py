def split_even_odd(arr):
  evens = [x for x in arr if x % 2 == 0]
  odds = [x for x in arr if x % 2 != 0]
  return evens, odds


# Example usage
numbers = [10, 5, 15, 4, 6, 20, 9]
even_arr, odd_arr = split_even_odd(numbers)

print("Original:", numbers)
print("Even Array:", even_arr)
print("Odd Array:", odd_arr)
