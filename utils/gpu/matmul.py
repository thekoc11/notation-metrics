from __future__ import division
from numba import cuda, float32
import numpy
import math

TPB = 16

#CUDA Kernel
@cuda.jit
def fast_matmul(A, B, C):

    #Define array in the shared memory
    # the size nad type of the arrays must be known in compile-time
    sA = cuda.shared.array(shape=(TPB, TPB), dtype=float32)
    sB = cuda.shared.array(shape=(TPB, TPB), dtype=float32)

    x, y = cuda.grid(2)

    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y

    if x >= C.shape[0] and y >= C.shape[1]:
        return
    # Each thread computes one element in the result matrix.
    # The dot product is chunked into dot products of TPB-long vectors
    tmp = 0
    for i in range(int(math.ceil(A.shape[0] / TPB))):
        # Preload data into shared memory
        sA[tx, ty] = A[x, ty + i * TPB]
        sB[tx, ty] = B[tx + i * TPB, y]

        # Wait until all threads finish preloading
        cuda.syncthreads()

        # computes partial product in the shared memory
        for j in range(TPB):
            tmp += sA[tx, j] * sB[j, ty]

        # Wait until all threads finish preloading
        cuda.syncthreads()

    C[x, y] = tmp


def Multiply(A, B):
    # A = numpy.full((TPB * 2 + 5, TPB * 3 + 11), 3, numpy.float) #matrix conatining all 3's
    # B = numpy.full((TPB * 3 + 11, TPB + 11), 4, numpy.float) # matrix containing all 4's

    A_global_mem = cuda.to_device(A)
    B_global_mem = cuda.to_device(B)

    #Allocate memory on the device for the result
    C_global_mem = cuda.device_array((A.shape[0], B.shape[1]))

    # Configure blocks
    threadsPerBlock = (TPB, TPB)
    blocksPerGrid_x = int(math.ceil(B.shape[0] / threadsPerBlock[0]))
    blocksPerGrid_y = int(math.ceil(A.shape[1] / threadsPerBlock[1]))
    blocksPerGrid = (blocksPerGrid_x, blocksPerGrid_y)

    print("Computing result using CUDA Kernel...\n")

    # MatrixMulCUDA[blocksPerGrid, threadsPerBlock](C_global_mem, A_global_mem, B_global_mem, A.shape[0], B.shape[0])
    fast_matmul[blocksPerGrid, threadsPerBlock](A_global_mem, B_global_mem, C_global_mem)
    print("Done !")
    res = C_global_mem.copy_to_host()
    return res

