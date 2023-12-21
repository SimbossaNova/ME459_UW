# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 13:03:37 2023

@author: jacob
"""

"Quick sort method "

def sorter(A):
    if len(A) <= 1:
        return A
    else:
        pivot = A[0]
        less = []
        greater = []
        for i in range(1, len(A)):
            if A[i] <= pivot:
                less.append(A[i])
            else:
                greater.append(A[i])
        return sorter(less) + [pivot] + sorter(greater)