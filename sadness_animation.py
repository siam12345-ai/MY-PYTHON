import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------
# PARAMETERS
# -----------------------------
S = 0.98          # sadness intensity (0-1)
T = 15            # total animation time
t = np.linspace(0, T, 400)

# Layers: body parts
layers = ["Torso", "Head", "Arms", "Legs", "Chakras", "Brain", "Heart", "Cells", "Atoms"]
heights = np.linspace(0.2, 1.8, len(layers))

# Colors for cinematic effect
colors = [
    (0.6,0.6,0.6),   # Torso gray
    (0.7,0.7,0.7),   # Head
    (0.5,0.5,0.5),   # Arms
    (0.5,0.5,0.5),   # Legs
    "cyan", "blue", "red", "pink", "violet"
]

# -----------------------------
# UTILITY FUNCTIONS
# -----------------------------
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

# Random positions for cells and atoms
num_cells = 30
cell_pos = np.random.uniform(-0.25, 0.25, (num_cells,3))
num_atoms = 80
atom_pos = np.random.uniform(-0.3,0.3, (num_atoms,3))

# Chakra positions along spine
chakra_pos = np.linspace(0.8, 1.7, 7)
chakra_colors = ["red","orange","yellow","green","blue","indigo","violet"]

# -----------------------------
# SETUP FIGURE
# -----------------------------
fig = plt.figure(figsize=(10, 12), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')

# -----------------------------
# UPDATE FUNCTION
# -----------------------------
def update(frame):
    ax.clear()
    time = t[frame]
    damping = (1 - S * time/T)  # sadness reduces amplitude
    
    # Cinematic camera rotation
    ax.view_init(elev=30 + 10*np.sin(0.05*time), azim=50 + 30*np.cos(0.03*time))
    
    # Torso
    xt, yt, zt = cylinder(0.8, 1.6, 0.25*damping)
    ax.plot_surface(xt, yt, zt, color=colors[0], alpha=0.6*damping)
    
    # Head
    xh, yh, zh = sphere(0.2*damping, z0=1.85)
    ax.plot_surface(xh, yh, zh, color=colors[1], alpha=0.7*damping)
    
    # Arms
    xa1, ya1, za1 = cylinder(1.2,0.8,0.08*damping, x0=0.35)
    xa2, ya2, za2 = cylinder(1.2,0.8,0.08*damping, x0=-0.35)
    ax.plot_surface(xa1, ya1, za1, color=colors[2], alpha=0.6*damping)
    ax.plot_surface(xa2, ya2, za2, color=colors[2], alpha=0.6*damping)
    
    # Legs
    xl1, yl1, zl1 = cylinder(0.8,0,0.1*damping, x0=0.12)
    xl2, yl2, zl2 = cylinder(0.8,0,0.1*damping, x0=-0.12)
    ax.plot_surface(xl1, yl1, zl1, color=colors[3], alpha=0.6*damping)
    ax.plot_surface(xl2, yl2, zl2, color=colors[3], alpha=0.6*damping)
    
    # Chakras as rings
    for i, zc in enumerate(chakra_pos):
        r = 0.12*damping
        theta = np.linspace(0,2*np.pi,30)
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        z = np.full_like(theta, zc)
        ax.plot(x,y,z,color=chakra_colors[i], linewidth=3, alpha=damping)
    
    # Brain & Heart spheres
    xb, yb, zb = sphere(0.08*damping, z0=1.85)
    ax.plot_surface(xb, yb, zb, color=colors[5], alpha=damping)
    xh_b, yh_b, zh_b = sphere(0.06*damping, z0=1.6)
    ax.plot_surface(xh_b, yh_b, zh_b, color=colors[6], alpha=damping)
    
    # Cells
    for pos in cell_pos:
        xc, yc, zc = sphere(0.015*damping, *pos)
        ax.plot_surface(xc, yc, zc, color=colors[7], alpha=damping)
    
    # Atoms
    for pos in atom_pos:
        xa, ya, za = sphere(0.005*damping, *pos)
        ax.plot_surface(xa, ya, za, color=colors[8], alpha=damping)
    
    ax.set_xlim(-0.6,0.6)
    ax.set_ylim(-0.6,0.6)
    ax.set_zlim(0,2.2)
    ax.set_title("Extreme Cinematic Sadness - 3D Full Body", color='white', fontsize=14)
    ax.axis('off')

# -----------------------------
# ANIMATION
# -----------------------------
ani = FuncAnimation(fig, update, frames=len(t), interval=60, cache_frame_data=False)
plt.show()
