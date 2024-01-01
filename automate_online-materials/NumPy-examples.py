import numpy as np

print(np.__version__)

# array with 10 zeros
#np.array([0] * 10)
print(np.zeros(10))
z10 = np.array([0] * 10)
print(z10)

# Create a numpy array with values ranging from 10 to 49
a10 = np.arange(10,50)
np.arange(10,50,2)
print(a10)

# Create a numpy matrix of 2*2 integers, filled with ones.
m10 = np.ones([2,2], dtype=np.int16)
print(m10)

# Create a numpy matrix of 3*2 float numbers, filled with ones.
