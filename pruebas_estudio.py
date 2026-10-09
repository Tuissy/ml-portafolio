import time
import numpy as np

a = np.ones((3, 2))        # forma (3, 2)
b = np.array([10, 20])     # forma (2,)
c = np.array([[10], [20], [30]]) # forma (1, 3)
c2 = c[np.newaxis, :]  # forma (3, 1)
d = np.array([1, 2, 3])    # forma (3,)

print(a + b)
print(a + c2)