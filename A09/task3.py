import random
import time

A = [[random.uniform(-1, 1) for j in range(1400)] for i in range(3400)]
B = [[random.uniform(-1, 1) for j in range(1400)] for i in range(3400)]

print(f"{A[-1][-1]}, {B[-1][-1]}")

start_time = time.time()
for i in range(3400):
    for j in range(1400):
        A[i][j], B[i][j] = B[i][j], A[i][j]
end_time = time.time()

print(f"{A[-1][-1]}, {B[-1][-1]}")

print(f"{round((end_time - start_time) * 1000, 2)} milliseconds.")

start_time = time.time()
for j in range(1400):
    for i in range(3400):
        A[i][j], B[i][j] = B[i][j], A[i][j]
end_time = time.time()

print(f"{A[-1][-1]}, {B[-1][-1]}")

print(f"{round((end_time - start_time) * 1000, 2)} milliseconds.")
