# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 21:13:24 2023

@author: jacob
"""

import random
from time import perf_counter
import argparse
import numpy as np
from sys import argv
from pyMatmul import matmul
import matplotlib.pyplot as plt
import sys 
import math 


parser = argparse.ArgumentParser(description='Input 0 or 1. 0 will not plot while 1 will plot')
parser.add_argument('integers',type=int, help='Please add 0 or 1 to work')
args = parser.parse_args()

if args.integers == 1:
    plotBool = True
elif args.integers == 0:
    plotBool = False
else:
    parser.error("Warning: Invalid input. Enter 0 or 1")


n= 2**5

A_list =[[random.uniform(-1, 1) for j in range(n)] for i in range(n)]
B_list= [[random.uniform(-1, 1) for j in range(n)] for i in range(n)]
  
A = np.array(A_list)
B = np.array(B_list)
    
tic = perf_counter()    
C = matmul(A_list, B_list)
tok = perf_counter()
time_C = tok - tic
time_C = time_C * 10**-3
    
#print("n = {}, time taken for A_list and B_list multiplication = {:.6f} seconds".format(n, time_C))

    
tic2 = perf_counter()    
C_np =  A @ B
tok2 = perf_counter()
time_Cnp = tok2 - tic2
time_Cnp = time_Cnp * 10**-3

#print("n = {}, time taken for A and B multiplication = {:.6f} seconds".format(n, time_Cnp))
   # print("--------------------------------")
   
   ####################################################################
   
   
n2= 2**6

A_list2 =[[random.uniform(-1, 1) for j in range(n2)] for i in range(n2)]
B_list2= [[random.uniform(-1, 1) for j in range(n2)] for i in range(n2)]
     
A2= np.array(A_list2)
B2 = np.array(B_list2)
       
tic = perf_counter()    
C2 = matmul(A_list2, B_list2)
tok = perf_counter()
time_C2 = tok - tic
time_C2 = time_C2 * 10**-3
       
 #print("n = {}, time taken for A_list and B_list multiplication = {:.6f} seconds".format(n, time))

       
tic2 = perf_counter()    
C2_np =  A2 @ B2
tok2 = perf_counter()
time_Cnp2 = tok2 - tic2
time_Cnp2 = time_Cnp2 * 10**-3

       
     #  print("n = {}, time taken for A and B multiplication = {:.6f} seconds".format(n, time2))
      # print("--------------------------------")
   
    
   ####################################################################
   
   
n3= 2**7

A_list3 =[[random.uniform(-1, 1) for j in range(n3)] for i in range(n3)]
B_list3= [[random.uniform(-1, 1) for j in range(n3)] for i in range(n3)]
     
A3= np.array(A_list3)
B3 =np.array(B_list3)
       
tic = perf_counter()    
C3 = matmul(A_list3, B_list3)
tok = perf_counter()
time_C3 = tok - tic
time_C3 = time_C3 * 10**-3
       
 #print("n = {}, time taken for A_list and B_list multiplication = {:.6f} seconds".format(n, time))

       
tic2 = perf_counter()    
C3_np =  A3 @ B3
tok2 = perf_counter()
time_Cnp3= tok2 - tic2
time_Cnp3 = time_Cnp3 * 10**-3


   ####################################################################
   
   
n4= 2**8

A_list4 =[[random.uniform(-1, 1) for j in range(n4)] for i in range(n4)]
B_list4= [[random.uniform(-1, 1) for j in range(n4)] for i in range(n4)]
     
A4= np.array(A_list4)
B4 = np.array(B_list4)
       
tic = perf_counter()    
C4 = matmul(A_list4, B_list4)
tok = perf_counter()
time_C4 = tok - tic
time_C4 = time_C4 * 10**-3
       
 #print("n = {}, time taken for A_list and B_list multiplication = {:.6f} seconds".format(n, time))
print(C4[0][0])
print(time_C4)
       
tic2 = perf_counter()    
C4_np =  A4 @ B4
tok2 = perf_counter()
time_Cnp4= tok2 - tic2
time_Cnp4 = time_Cnp4 * 10**-3
print(C4_np[0][0])
print(time_Cnp4)

####################################################################

if (plotBool==True): 
    x = [math.log2(n), math.log2(n2), math.log2(n3), math.log2(n4)]
    
    y_list = [ math.log10(time_C) , math.log10(time_C2), math.log10(time_C3), math.log10(time_C4)]
    
    y_numpy=[ math.log10(time_Cnp) , math.log10(time_Cnp2), math.log10(time_Cnp3), math.log10(time_Cnp4)]
    
    
    plt.plot(x, y_list, label='n vs list multiplcation ')
    plt.plot(x, y_numpy, label='n vs numpy multiplcation ')
    plt.xlabel('log2(n)')
    plt.ylabel('log10(time taken in ms)')
    plt.title(' Time [log10(ms)] vs n [log2(n)] for matmulCompare')
    plt.legend()
    plt.show()