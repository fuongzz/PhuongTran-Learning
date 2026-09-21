import numpy as np

import time

def my_dot(a, b):
    x = 0
    for i in range(a.shape[0]):
        x = x + a[i] * b[i]
    return x

np.random.seed(1)

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a, b)
toc = time.time()

print(f"c = {c}")
print(f"Time cost: {1000*(toc-tic):.4f} ms")

tic = time.time()
c = my_dot(a, b)
toc = time.time()

print(f"my_dot(a, b) = {c:.4f}")
print(f"loop version duration: {1000*(toc-tic):.4f} ms")
