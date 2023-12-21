# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:40:13 2023

@author: jacob
"""

import random
from time import perf_counter
import argparse
import numpy as np
from sys import argv
import matplotlib.pyplot as plt
import sys 
import math 

fig, ax = plt.subplots()
ax.set_yscale('linear')

n = 2**5
n2=2**6
n3=2**7
n4=2**8
n5=2**9
n6=2**10

t1_n = 0.3
t1_n2= 1.4
t1_n3= 10.9
t1_n4 = 154.5
t1_n5 = 1757.4
t1_n6 =  16083






x = [math.log2(n), math.log2(n2), math.log2(n3),math.log2(n4), math.log2(n5), math.log2(n6)]

y_t1 = [ (t1_n) , (t1_n2), (t1_n3), (t1_n4), (t1_n5), (t1_n6)]



plt.plot(x, y_t1, label=' mmul1 ')
#plt.plot(x, y_t2, label=' sumArray2')
plt.xlabel('n (log scale)')
plt.ylabel('time taken in ms (linear scale)')
plt.title(' Time [(ms) log scale] vs n for mmul1')
plt.legend()
plt.show()