import numpy as np

arr = np.array([[[241, 33, 41], [444, 22, 10], [342, 122, 315]]])

print(arr)
print(arr[0, 0, 1])

third_column_sum = np.sum(arr[0, :, 2])
print("Sum of third column: ")
print(third_column_sum)
