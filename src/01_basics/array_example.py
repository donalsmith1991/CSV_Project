# Lists cannot be multiplied together.
list_a = [1, 2, 3]
list_b = [2, 4, 6]


# NumPy arrays let you perform array operations.

# Import numpy, aliased as np.
import numpy as np

# Convert lists to arrays.
array_a = np.array(list_a)
array_b = np.array(list_b)

# Perform element-wise multiplication between the arrays.
array_a * array_b
my_array=(array_a * array_b).tolist()
print(my_array)
np.array([2, 4, 6])
print(np.array([2, 4, 6]))
