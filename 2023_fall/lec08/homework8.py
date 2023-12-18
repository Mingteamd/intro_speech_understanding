import numpy as np

def dft_matrix(N):
    '''
    Create a DFT transform matrix, W, of size N.
    
    @param:
    N (scalar): number of columns in the transform matrix
    
    @result:
    W (NxN array): a matrix of dtype='complex' whose (k,n)^th element is:
           W[k,n] = cos(2*np.pi*k*n/N) - j*sin(2*np.pi*k*n/N)
    '''
    # Initialize the DFT matrix
    W = np.zeros((N, N), dtype=np.complex128)

    # Populate the DFT matrix
    for k in range(N):
        for n in range(N):
            W[k, n] = np.cos(2 * np.pi * k * n / N) - 1j * np.sin(2 * np.pi * k * n / N)

    return W

# Example usage:
N = 4
DFT_matrix = dft_matrix(N)
print(DFT_matrix)
