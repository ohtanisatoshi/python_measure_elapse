import numpy as np
from measure_elapse import measure_elapse

@measure_elapse
def generate_vector(v1_c, v2_c, d):
    a = np.random.rand(v1_c, d)
    b = np.random.rand(v2_c, d)
    return a, b

@measure_elapse
def dot(a, b):
    return np.dot(a, b.T)

if __name__ == '__main__':
    a, b = generate_vector(10000000, 50, 300)
    dot(a, b)
