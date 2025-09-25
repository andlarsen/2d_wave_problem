# The program Heat_1D solves the 1D heat equation with the forward difference 
# method (the explicit method).

import numpy as np
import matplotlib.pyplot as plt

# Solves the 1D unsteady-state heat equation using the forward difference method
# The heat equation in terms of u = u(x,t) is given as        
#                                u   = u                      
#                                 t     xx                    
# For this example:                                           
#   Initial conditions           u(x,0) = f(x) = sin(PI x)    
#   Boundary conditions          u(0,t) = u(1,t) = 0          
#                                                             
# The coordinate x belongs to the interval: 0 <= x <= 1       
# The time t belongs to the interval      : 0 <= t <= tEnd                                                   

n = int(input('Number of points in the x- and y-direction: '))
m = n
#m = input('Number of points in the y-direction, m: ');

r = float(input('Enter the ratio r (has to be smaller than 1/2), r*: '))
h = 1.0/(float(n)-1)
k = np.sqrt(r*h**2)

# Initialize the matrix u containing u(i,j) to 0.0
if r < 0.0 or r > 1/2:
  print('r = %d, i.e. the algorithm is unstable!', r)
  print('You have to reduce the time step size or increase the coordinate step size')
  exit()

nTimeSteps = int(input('Enter the number of time steps, nTimeSteps: '))
g = float(input('Initial velocity, g: '))

# Initializes the matrices
u = np.zeros((n,m))
u_k = np.zeros((n,m))
u_k_minus = np.zeros((n,m))

# Sets up the initial boundary conditions
#u_k(1:n,1:m) = Wave_2D_BCs(n, m, u_k)

# Solves the equations and plots the result on a contour plot
#u = Wave_2D_Solver(n, m, u, u_k, u_k_minus, nTimeSteps, r, h, k, g)

