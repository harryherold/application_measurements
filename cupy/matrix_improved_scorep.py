#!/usr/bin/env python

import numpy as np
import cupy as cp
import random
import scorep as sp

def load_matrix(size: int) -> cp.array:
    return cp.random.uniform(low=42.0, high=1337.0, size=(size, size), dtype=float)

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
