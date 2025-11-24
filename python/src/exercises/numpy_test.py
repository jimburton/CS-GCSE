import numpy as np
# Create an array
data = np.array([2, 5, 8, 10])
print(data.shape)

# Operations
data = data * 2
print(data)
data[data > 15] = 99
print(data)
data = data[0:3]

print(data.shape)
print(data)