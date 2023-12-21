# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 13:55:08 2023

@author: jacob
"""

import numpy as np
import sys
from pySort import sorter
import random
from time import perf_counter
import math 
import matplotlib.pyplot as plt
import argparse



parser = argparse.ArgumentParser(description='Input 0 or 1. 0 will not plot while 1 will plot')
parser.add_argument('integers',type=int,help='Please add 0 or 1 to work')
args = parser.parse_args()

if args.integers == 1:
    plotBool = True
elif args.integers == 0:
    plotBool = False
else:
    parser.error("Warning: Invalid input. Enter 0 or 1")

n = 2**10
A_list = [random.randint(-10, 10) for _ in range(n)]
B_list = A_list.copy()
A = np.array(A_list)


tic = perf_counter()    
C = sorter(A_list)
tok = perf_counter()
time_C = tok - tic
time_C = time_C * 10**-3
#print(time_C)

tic = perf_counter() 
B_list.sort()
tok = perf_counter() 
time_C1 = tok - tic
time_C1 = time_C1 * 10**-3
#print(time_C1)

tic = perf_counter() 
A_sorted = np.sort(A)
tok = perf_counter() 
time_C2 = tok - tic
time_C2 = time_C2 * 10**-3
#print(time_C2)

########################################################################

n2 = 2**11
A_list2 = [random.randint(-10, 10) for _ in range(n2)]
B_list2 = A_list2.copy()
A2= np.array(A_list2)


tic = perf_counter()    
C3 = sorter(A_list2)
tok = perf_counter()
time_C3 = tok - tic
time_C3 = time_C3 * 10**-3
#print(time_C3)

tic = perf_counter() 
B_list2.sort()
tok = perf_counter() 
time_C4 = tok - tic
time_C4 = time_C4 * 10**-3
#print(time_C4)

tic = perf_counter() 
A_sorted2 = np.sort(A2)
tok = perf_counter() 
time_C5 = tok - tic
time_C5 = time_C5 * 10**-3
#print(time_C5)


########################################################################

n3 = 2**12
A_list3 = [random.randint(-10, 10) for _ in range(n3)]
B_list3 = A_list3.copy()
A3= np.array(A_list3)


tic = perf_counter()    
C6 = sorter(A_list3)
tok = perf_counter()
time_C6 = tok - tic
time_C6 = time_C6 * 10**-3
#print(time_C6)

tic = perf_counter() 
B_list3.sort()
tok = perf_counter() 
time_C7 = tok - tic
time_C7 = time_C7 * 10**-3
#print(time_C7)

tic = perf_counter() 
A_sorted3 = np.sort(A3)
tok = perf_counter() 
time_C8 = tok - tic
time_C8 = time_C8 * 10**-3
#print(time_C8)

########################################################################

n4 = 2**13
A_list4 = [random.randint(-10, 10) for _ in range(n4)]
B_list4 = A_list4.copy()
A4= np.array(A_list4)


tic = perf_counter()    
C9 = sorter(A_list4)
tok = perf_counter()
time_C9 = tok - tic
time_C9 = time_C9 * 10**-3
#print(time_C9)

tic = perf_counter() 
B_list4.sort()
tok = perf_counter() 
time_C10 = tok - tic
time_C10 = time_C10 * 10**-3
#print(time_C10)

tic = perf_counter() 
A_sorted4= np.sort(A4)
tok = perf_counter() 
time_C11 = tok - tic
time_C11 = time_C11 * 10**-3
#print(time_C11)

########################################################################

n5 = 2**14
A_list5 = [random.randint(-10, 10) for _ in range(n5)]
B_list5 = A_list5.copy()
A5= np.array(A_list5)


tic = perf_counter()    
C12 = sorter(A_list5)
print (C12[0])
tok = perf_counter()
time_C12 = tok - tic
time_C12 = time_C12 * 10**-3
print(time_C12)

tic = perf_counter() 
B_list5.sort()
print (B_list5[0])
tok = perf_counter() 
time_C13 = tok - tic
time_C13 = time_C13 * 10**-3
print(time_C13)

tic = perf_counter() 
A_sorted5= np.sort(A5)
print(A_sorted5[0])
tok = perf_counter() 
time_C14 = tok - tic
time_C14 = time_C14 * 10**-3
print(time_C14)

####################################################################

if (plotBool==True): 

    x = [math.log2(n), math.log2(n2), math.log2(n3), math.log2(n4), math.log2(n5)]
    
    y_list = [ math.log10(time_C) , math.log10(time_C3), math.log10(time_C6), math.log10(time_C9), math.log10(time_C12)]
    
    y_copy = [ math.log10(time_C1) , math.log10(time_C4), math.log10(time_C7), math.log10(time_C10), math.log10(time_C13)]
    
    y_numpy=[ math.log10(time_C2) , math.log10(time_C5), math.log10(time_C8), math.log10(time_C11), math.log10(time_C14)]
    
    
    plt.plot(x, y_list, label='n vs pySort sorter  ')
    
    plt.plot(x, y_copy, label='n vs built in python sort function ')
    
    plt.plot(x, y_numpy, label='n vs numpy sorter ')
    
    plt.xlabel('log2(n)')
    plt.ylabel('log10(time taken in ms)')
    plt.title(' Time [log10(ms)] vs n [log2(n)] for sorterCompare')
    plt.legend()
    plt.show()
    
