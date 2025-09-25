import numpy as np

def setup_boundary_conditions(n: int, m: int, u_k: np.ndarray) -> np.ndarray:
    # This function is called from PlateTen and is used for defining the boundary conditions.
    # Input: n is the number of points in the x-direction
    #        m is the number of points in the y-direction
    #        h is the mesh size
    #        u contains u(i,j) that has been initialized
        # Output: u has been updated with the boundary values
    for i in range(1, n-1):       # Python uses 0-based indexing
            for j in range(1, m-1):
                x = i / (n - 1)
                y = j / (m - 1)
                u_k[i, j] = np.sin(np.pi * x) * np.sin(np.pi * y)
        
    return u_k