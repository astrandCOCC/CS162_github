import numpy as np

# Generates a 5x5 array of numbers 1-10:
arr = np.random.randint(0, 11, size=(5, 5))

# Print the array:
print("Array: ")
print(arr)

# Print the randomly generated number on the -
# 2nd row, 3rd column:
print(arr[1, 2])

# Print the sum of all elements in the array:
arr_sum = np.sum(arr)
print("Sum of all elements:", arr_sum)

# Print the mean of each row in the array:
row_means = np.mean(arr, axis=1)
print("Mean of each row:")
print(row_means)
