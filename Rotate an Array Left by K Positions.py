def rotate_left(arr, k):
  n = len(arr)
  if n == 0:
    return arr
  k = k % n  # Handle rotations greater than array length
  return arr[k:] + arr[:k]


# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
k_steps = 2
print("Rotated Array:", rotate_left(arr, k_steps))
