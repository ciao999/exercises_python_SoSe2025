import numpy as np

a = np.arange(1, 13)

#print(a.reshape(3, 2, 2))  #3 Dimensionen vom array muss passen

a_reshaped = a.reshape(3, 2, 2)

print(a_reshaped.ndim)
print(a_reshaped.shape)
print(a_reshaped.size)
print(a_reshaped.dtype)

