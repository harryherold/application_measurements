#!/usr/bin/env python

import numpy as np
import cupy as cp
import random


def load_matrix(size: int) -> cp.array:
    data = []
    for i in range(size):
        data.append([random.uniform(42.0, 1337.0) for _ in range(size)])
    return cp.array(data, ndmin=2)


SIZE = 1024
N = 6
np.random.seed(0)


for i in range(N):
    A = load_matrix(SIZE)
    B = load_matrix(SIZE)
    cp.dot(A, B)
    del A, B

cp.cuda.Stream.null.synchronize()
