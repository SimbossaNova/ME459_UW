# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 13:25:33 2023

@author: jacob
"""
import random
from time import perf_counter
from pySort import sorter


n_values = [10**3, 10**4, 10**5, 10**6 ]

for n in n_values:
    A = [random.random() for _ in range(n)]
    
    tic = perf_counter()    
    C = sorter(A)
    tok = perf_counter()
    time = tok - tic
    
    print("n = {}, time taken = {:.6f} seconds".format(n, time))
    

