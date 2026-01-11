import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Sadness intensity
S = 0.85

fig = plt.figure(figsize=(7, 9))
ax = fig.add_subplot(111, projection='3d')

# Cylinder function (body parts)
def cylinder(z_start, z_end, radius, x0=0, y0=0):
    z = np.linspace(z_start, z_end, 30)
    theta = np.linspace(0, 2*np.pi, 30)
    theta, z = np.meshgrid(theta, z)
    x = radius * np.cos(theta) + x0
    y = radius * np.sin(theta) + y0
    return x, y, z

def update(frame):
    ax.clear()
    t = frame / 10
    damping = np.exp(-S * t)

    # Head
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:20j]
    xh = 0.25*damping*np.cos(u)*np.sin(v)
    yh = 0.25*damping*np.sin(u)*np.sin(v)
    zh = 1.75 + 0.25*damping*np.cos(v)
    ax.plot_surface(xh, yh, zh, alpha=0.7)

    # Torso
    xt, yt, zt = cylinder(0.8, 1.6, 0.3*damping)
    ax.plot_surface(xt, yt, zt, alpha=0.6)

    # Arms
    xa1, ya1, za1 = cylinder(1.2, 0.6, 0.1*damping, x0=0.45)
    xa2, ya2, za2 = cylinder(1.2, 0.6, 0.1*damping, x0=-0.45)
    ax.plot_surface(xa1, ya1, za1, alpha=0.6)
    ax.plot_surface(xa2, ya2, za2, alpha=0.6)

    # Legs
    xl1, yl1, zl1 = cylinder(0.8, 0, 0.12*damping, x0=0.15)
    xl2, yl2, zl2 = cylinder(0.8, 0, 0.12*damping, x0=-0.15)
    ax.plot_surface(xl1, yl1, zl1, alpha=0.6)
    ax.plot_surface(xl2, yl2, zl2, alpha=0.6)

    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(0, 2)
    ax.set_title("3D Human Body Under Sadness (System-Wide Damping)")
    ax.axis('off')

ani = FuncAnimation(
    fig,
    update,
    frames=120,
    interval=60,
    cache_frame_data=False
)

plt.show()
