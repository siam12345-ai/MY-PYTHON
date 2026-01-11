import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Extreme sadness
S = 0.98
T = 15
t = np.linspace(0, T, 400)

fig = plt.figure(figsize=(10, 12), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')

# Body parts: torso + head + arms + legs
def cylinder(z_start, z_end, radius, x0=0, y0=0, n=20):
    z = np.linspace(z_start, z_end, n)
    theta = np.linspace(0, 2*np.pi, n)
    theta, z = np.meshgrid(theta, z)
    x = radius*np.cos(theta) + x0
    y = radius*np.sin(theta) + y0
    return x, y, z

def sphere(radius, x0=0, y0=0, z0=0, n=20):
    u, v = np.mgrid[0:2*np.pi:n*1j, 0:np.pi:n*1j]
    x = radius*np.cos(u)*np.sin(v) + x0
    y = radius*np.sin(u)*np.sin(v) + y0
    z = radius*np.cos(v) + z0
    return x, y, z

# Layers
chakras_pos = np.linspace(0.8, 1.7, 7)
chakra_colors = ["red","orange","yellow","green","blue","indigo","violet"]

# Cells / atoms positions
num_cells = 30
cell_pos = np.random.uniform(-0.3,0.3,(num_cells,3))
num_atoms = 80
atom_pos = np.random.uniform(-0.35,0.35,(num_atoms,3))

def update(frame):
    ax.clear()
    time = t[frame]
    damping = (1 - S*time/T)
    
    # Cinematic camera rotation
    ax.view_init(elev=30+10*np.sin(0.05*time), azim=50+30*np.cos(0.03*time))
    
    # Torso
    xt, yt, zt = cylinder(0.8,1.6,0.25*damping)
    ax.plot_surface(xt, yt, zt, color='gray', alpha=0.6*damping)
    
    # Head
    xh, yh, zh = sphere(0.2*damping, z0=1.85)
    ax.plot_surface(xh, yh, zh, color='lightgray', alpha=0.7*damping)
    
    # Arms
    xa1, ya1, za1 = cylinder(1.2,0.8,0.08*damping, x0=0.35)
    xa2, ya2, za2 = cylinder(1.2,0.8,0.08*damping, x0=-0.35)
    ax.plot_surface(xa1, ya1, za1, color='gray', alpha=0.6*damping)
    ax.plot_surface(xa2, ya2, za2, color='gray', alpha=0.6*damping)
    
    # Legs
    xl1, yl1, zl1 = cylinder(0.8,0,0.1*damping, x0=0.12)
    xl2, yl2, zl2 = cylinder(0.8,0,0.1*damping, x0=-0.12)
    ax.plot_surface(xl1, yl1, zl1, color='gray', alpha=0.6*damping)
    ax.plot_surface(xl2, yl2, zl2, color='gray', alpha=0.6*damping)
    
    # Chakras
    for i, zc in enumerate(chakras_pos):
        r = 0.12*damping
        theta = np.linspace(0,2*np.pi,30)
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        z = np.full_like(theta, zc)
        ax.plot(x,y,z,color=chakra_colors[i], linewidth=3, alpha=damping)
    
    # Heart + brain spheres
    xh_b, yh_b, zh_b = sphere(0.06*damping, z0=1.6)
    ax.plot_surface(xh_b, yh_b, zh_b, color='red', alpha=damping)
    xb, yb, zb = sphere(0.08*damping, z0=1.85)
    ax.plot_surface(xb, yb, zb, color='blue', alpha=damping)
    
    # Cells
    for pos in cell_pos:
        xc, yc, zc = sphere(0.015*damping, *pos)
        ax.plot_surface(xc, yc, zc, color='pink', alpha=damping)
    
    # Atoms
    for pos in atom_pos:
        xa, ya, za = sphere(0.005*damping, *pos)
        ax.plot_surface(xa, ya, za, color='violet', alpha=damping)
    
    ax.set_xlim(-0.6,0.6)
    ax.set_ylim(-0.6,0.6)
    ax.set_zlim(0,2.2)
    ax.set_title("Extreme Deep Cinematic Sadness - Full Body 3D", color='white', fontsize=14)
    ax.axis('off')

ani = FuncAnimation(fig, update, frames=len(t), interval=60, cache_frame_data=False)
plt.show()
