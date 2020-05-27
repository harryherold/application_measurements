import numpy as np
import random
import scorep


def load_matrix(size: int) -> np.array:
    return np.random.uniform(42.0, 1337.0, size=(size, size))


with scorep.user.region("init"):
    SIZE = 1024
    N = 4
    np.random.seed(0)

scorep.user.region_begin("compute")
for _ in range(N):
    A = load_matrix(SIZE)
    B = load_matrix(SIZE)
    C = np.dot(A, B)
    del A, B
scorep.user.region_end("compute")
