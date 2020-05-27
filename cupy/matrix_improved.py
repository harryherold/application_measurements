#!/usr/bin/env python

import numpy as np
import cupy as cp
import random

def load_matrix(size: int) -> cp.array:
    return cp.random.uniform(low=42.0, high=1337.0, size=(size, size), dtype=float)

SIZE = 1024
N = 6
np.random.seed(0)

for i in range(N):
    A = load_matrix(SIZE)
    B = load_matrix(SIZE)
    cp.dot(A, B)
    del A, B

cp.cuda.Stream.null.synchronize()
