# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:01:53 2023

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

fig, ax = plt.subplots()
ax.set_xscale('log')
ax.set_yscale('linear')

n = 2**7
n2=2**8
n3=2**9
n4=2**10
n5=2**11
n6=2**12

t1_n = 0.045
t1_n2= 0.203
t1_n3=0.896
t1_n4 = 4.344
t1_n5 = 14.799
t1_n6 = 52.237

t2_n = 0.044
t2_n2 = 0.215
t2_n3 = 1.577
t2_n4 = 16.651
t2_n5 = 75.492
t2_n6 = 175.495




x = [(n), (n2), (n3),(n4), (n5), (n6)]

y_t1 = [ (t1_n) , (t1_n2), (t1_n3), (t1_n4), (t1_n5), (t1_n6)]

y_t2= [ (t2_n) , (t2_n2), (t2_n3), (t2_n4), (t2_n5), (t2_n6)]


plt.plot(x, y_t1, label=' sumArray1 ')
plt.plot(x, y_t2, label=' sumArray2')
plt.xlabel('n')
plt.ylabel('time taken in ms')
plt.title(' Time [(ms)] vs n for task2.C')
plt.legend()
plt.show()