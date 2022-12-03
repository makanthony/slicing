# -*- coding: utf-8 -*-
"""
Dec 2 2022

Anthony Mak
"""

import numpy as np

A = np.array(np.zeros((3, 7)))

for i in range(3):
    for j in range(7):
        A[i, j] = i*j

print("array A\n", A) 
print("\nrow 2 of A\n", A[2])#does row 2 mean second row or index 2? doing index because you did not specify
print("\nrow 2 of A in reverse order\n", A[2, ::-1])
print("\nthe sub-matrix consisting or the bottom right 2x2 sub-array\n", A[1:3, 5:7])
print("\nthe sub-array consisting of the bottom left 2x2 sub-array\n", A[1:3, 0:2])
print("\nthe 3x3 sub-array in the middle of A\n", A[0:3, 2:5])


