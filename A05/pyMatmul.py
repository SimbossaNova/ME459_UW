# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:10:43 2023s

@author: jacob 
"""

def matmul(A, B):
    n = len(A)
    result = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            val = 0
            for k in range(n):
                val += A[i][k] * B[k][j]
            result[i].append(val)
    return result