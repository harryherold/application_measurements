import numpy as np
import random
import scorep


def load_matrix(size: int) -> np.matrix:
    data = []
    for i in range(size):
        data.append([random.uniform(42.0, 1337.0) for _ in range(size)])
    return np.matrix(data)


scorep.user.region_begin("initialization")

SIZE = 1024
N = 4
np.random.seed(0)

scorep.user.region_end("initialization")

scorep.user.region_begin("compute")
for i in range(N):
    A = load_matrix(SIZE)
    B = load_matrix(SIZE)
    C = np.dot(A, B)
    del A, B
scorep.user.region_end("compute")
