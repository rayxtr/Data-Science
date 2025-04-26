# %% [markdown]
# ##NUMPY
# 
# numpy aims to provide  an array  object that is upto 50 x faster than traditional lists.
# Numpy arrays are stored at one continous place in memory unlike lists so processes can access and manipulate them very efficiently.

# %%
import numpy as np;
a = np.array([1,2,22,3])

# %%
for i in range (len(a)):
    print(i*7)

# %%
import numpy as np;
# Create a 2D array
matrix = np.array([[1, 2], [3, 4]])
print("2D Array:\n", matrix)

# Accessing elements
print("Element at row 0, column 1:", matrix[0, 1])  # Output: 2
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)        # [11 22 33]
print("Multiplication:", a * b)  # [10 40 90]
print("Mean of a:", np.mean(a))  # 20.0



# %%
import numpy as np;
# Create a 3x3 matrix with random values
rand_matrix = np.random.rand(3, 3)
print("Random Matrix:\n", rand_matrix)

# Reshape a flat array to 2D
flat = np.arange(9)
reshaped = flat.reshape(3, 3)
print("Reshaped Array:\n", reshaped)


# %%
import numpy as np;
arr = np.array([5, 10, 15, 20, 25])
filtered = arr[arr > 15]
print("Filtered (greater than 15):", filtered)  # [20 25]


# %%
import numpy as ss;
arr1 = ss.array([2,3,4,5,5]);
for i in range (len(arr1)):
    if i==1 :
        print(arr1[i])


# %%
import numpy as np

# Step 1: Define two arrays
array1 = [1, 3, 5, 7, 9]
array2 = [2, 3, 5, 8, 10]

# Step 2: Get the union (remove duplicates)
union_array = list(set(array1 + array2))
union_array.sort()

# Step 3: Calculate mean and median
mean_val = np.mean(union_array)
median_val = np.median(union_array)

# Step 4: Print results
print("Array 1:", array1)
print("Array 2:", array2)
print("Union:", union_array)
print("Mean:", mean_val)
print("Median:", median_val)


# %%
from math import isqrt
import numpy as np;

# Arrays
array1 = [2, 3, 4]
array2 = [1, 2, 3]

# Union and sort
union_array = sorted(set(array1 + array2))

print("Star Patterns:\n")

# Function to print a star block of given rows and cols
def print_block(rows, cols):
    for _ in range(rows):
        print("*" * cols)
    print()

# Generate all rectangle patterns for each number
for num in union_array:
    print(f"Patterns for {num} stars:")
    for rows in range(1, num + 1):
        if num % rows == 0:
            cols = num // rows
            print_block(rows, cols)


# %%



