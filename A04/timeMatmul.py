import random
from time import perf_counter
from pyMatmul import matmul

n_values = [2**7, 2**8, 2**9]

for n in n_values:
    A = [[random.random() for _ in range(n)] for _ in range(n)]
    B = [[random.random() for _ in range(n)] for _ in range(n)]
    
    tic = perf_counter()    
    C = matmul(A, B)
    tok = perf_counter()
    time = tok - tic
    
    print("n = {}, time taken = {:.6f} seconds".format(n, time))