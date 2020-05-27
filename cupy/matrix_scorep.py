#!/usr/bin/env python

import numpy as np
import cupy as cp
import random
import scorep as sp

def load_matrix(size: int) -> cp.array:
    data = []
    for i in range(size):
        data.append([random.uniform(42.0, 1337.0) for _ in range(size)])
    return cp.array(data, ndmin=2)

with sp.user.region("init"):
    SIZE = 1024
    N = 6
    np.random.seed(0)

sp.user.region_begin("compute")
for i in range(N):
    A = load_matrix(SIZE)
    B = load_matrix(SIZE)
    cp.dot(A, B)
    del A, B
sp.user.region_end("compute")

with sp.user.region("gpu_sync"):
    cp.cuda.Stream.null.synchronize()

