import numpy as np
import matplotlib.pyplot as plt

def solver(n: int, m: int, u: np.ndarray, u_k: np.ndarray, u_k_minus: np.ndarray, nTimeSteps: int, r: float, h: float, k: float, g: float, iter: int) -> np.ndarray:
    #  This function is called from PlateTen and is used for solving the biharmonic equation
    # using the S.O.R. solution method.
    # Input: n is the number of points in the x-direction
    #        m is the number of points in the y-direction
    #        u contains u(i,j) with boundary conditions defined
    # Output: u contains the solution to the problem

    for i in range(1,n-1):
        for j in range(1,m-1):
            if iter == 1:
                u[i,j] = 1/2 * (2*u_k[i,j]- ( 2*k*g ) + r*( u_k[i+1,j]+u_k[i-1,j]+u_k[i,j+1]+u_k[i,j-1]-4*u_k[i,j] ))
            else:
                u[i,j] = 2*u_k[i,j]-u_k_minus[i,j] + r*( u_k[i+1,j]+u_k[i-1,j]+u_k[i,j+1]+u_k[i,j-1]-4*u_k[i,j] )
            
    u_k_minus = np.copy(u_k)
    u_k = np.copy(u)

    return u_k, u_k_minus

