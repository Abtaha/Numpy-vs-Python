import random
import numpy as np
import time
import matplotlib.pyplot as plt


def py_mul(n):
    A = [[random.randrange(1, 1000) for i in range(n)] for j in range(n)]
    B = [[random.randrange(1, 1000) for i in range(n)] for j in range(n)]
    
    result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

def np_mul(n):
    A = np.random.randint(low = 0, high = 1000,size = (n, n))
    B = np.random.randint(low = 0, high = 1000,size = (n, n))
    
    result = np.matmul(A, B)

def main():
    py_multiply = []
    np_multiply = []
    
    for n in range(0, 1000, 50):#np.logspace(1, 4, num = 4, dtype=int):
        start = time.time()
        py_mul(n)
        taken = time.time() - start
        py_multiply.append([n, taken])

        start = time.time()
        np_mul(n)
        taken = time.time() - start
        np_multiply.append([n, taken])
    
    plt.plot([item[0] for item in py_multiply], [item[1] for item in py_multiply], color="green", label="Python")
    plt.plot([item[0] for item in np_multiply], [item[1] for item in np_multiply], color="red", label="Numpy")
    
    plt.title("Matrix Multiplication")
    plt.xlabel("Input")
    plt.ylabel("Time")
    plt.legend(loc="upper left")
    
    plt.show()
    
if __name__ == "__main__":
    main()