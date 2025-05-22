import math
import numpy as np
x =   [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]

x_log = []

for zahl in x: 
    x_log.append(math.log10(zahl))
 
print(x_log)



x_array = np.array(x)
log_array = np.log10(x_array)


print("Logarithmus mit numpy.log10():")
print(log_array)

