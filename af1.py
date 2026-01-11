import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
t = np.linspace(0, 4*np.pi, 200)
theta = np.linspace(0, 2*np.pi, 40)
T, TH = np.meshgrid(t, theta)

frequency = 0.04

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def update(frame):
    ax.clear()

    # DNA core
    x1 = np.cos(t + frame * frequency)
    y1 = np.sin(t + frame * frequency)
    z = t

    x2 = np.cos(t + frame * frequency + np.pi)
    y2 = np.sin(t + frame * frequency + np.pi)

    # Aura radius breathing
    aura_radius = 1.2 + 0.3 * np.sin(frame * frequency)

    # Aura field surface
    X = aura_radius * np.cos(TH)
    Y = aura_radius * np.sin(TH)
    Z = T

    glow = (np.sin(frame * frequency) + 1) / 2
    aura_color = (glow, 0.3, 1 - glow)

    # Plot aura
    ax.plot_surface(
        X, Y, Z,
        color=aura_color,
        alpha=0.25,
        linewidth=0
    )

    # Plot DNA
    ax.plot(x1, y1, z, color='white', linewidth=2)
    ax.plot(x2, y2, z, color='white', linewidth=2)

    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(0, 4*np.pi)

    ax.set_title("DNA with Living Aura Field", color=aura_color)

ani = FuncAnimation(fig, update, interval=50)
plt.show()
