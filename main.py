import imageio
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from boundary import setup_boundary_conditions
from solver import solver

frames = []  # list to store each frame as an image

# Initialize arrays 
n, m = 50, 50
r = 0.1
h = 1.0 / (n - 1)
k = r * h**2
nTimeSteps = 200
g = 0.5

u = np.zeros((n, m))
u_k = np.zeros((n, m))
u_k_minus = np.zeros((n, m))
u_k = setup_boundary_conditions(n, m, u_k)

u_min = -1.0
u_max = 1.0

# Time-stepping loop
for iteration in range(1, nTimeSteps + 1):
    u_k, u_k_minus = solver(n, m, u, u_k, u_k_minus, nTimeSteps, r, h, k, g, iteration)
    
    # Save frame
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(np.linspace(0, 1, n), np.linspace(0, 1, m))
    surf = ax.plot_surface(X, Y, u_k, cmap='viridis', alpha=0.8)
    ax.set_title(f'Time Step: {iteration} of {nTimeSteps}')
    
    # Set consistent viewing angle and limits for better animation
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('u(x,y,t)')
    ax.view_init(elev=30, azim=45)  # Set viewing angle
    
    # Optional: set consistent z-limits if you know the range
    ax.set_zlim([u_min, u_max])  # uncomment and set appropriate values
    
    # Ensure the figure is rendered before extracting image data
    fig.canvas.draw()
    
    # Convert figure to image array
    image = np.frombuffer(fig.canvas.buffer_rgba(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (4,))
    # Convert RGBA to RGB by removing alpha channel
    image = image[:, :, :3]
    frames.append(image)
    
    # Close figure after extracting image data
    plt.close(fig)

# Save the GIF after all frames are collected
imageio.mimsave('2d_wave_simulation.gif', frames, fps=10)
print("Saved GIF as 2d_wave_simulation.gif")