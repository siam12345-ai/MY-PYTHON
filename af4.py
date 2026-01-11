import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# Base structure
t = np.linspace(0, 4*np.pi, 200)
theta = np.linspace(0, 2*np.pi, 40)
T, TH = np.meshgrid(t, theta)

# Chakra data
chakras = [
    ("Root", 0.02, (1, 0, 0)),
    ("Sacral", 0.03, (1, 0.5, 0)),
    ("Solar", 0.04, (1, 1, 0)),
    ("Heart", 0.05, (0, 1, 0)),
    ("Throat", 0.06, (0, 0.5, 1)),
    ("Third Eye", 0.07, (0.3, 0, 0.5)),
    ("Crown", 0.08, (0.6, 0, 1))
]

# Figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)

# Slider
ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
chakra_slider = Slider(ax_slider, "Chakra", 0, 6, valinit=3, valstep=1)

def update(frame):
    ax.clear()

    idx = int(chakra_slider.val)
    name, frequency, color = chakras[idx]

    # Mutation strength
    mutation = 0.3 * frequency * np.sin(frame * frequency)

    # DNA (mutating)
    x1 = np.cos(t + frame * frequency) * (1 + mutation)
    y1 = np.sin(t + frame * frequency) * (1 + mutation)
    z = t

    x2 = np.cos(t + frame * frequency + np.pi) * (1 - mutation)
    y2 = np.sin(t + frame * frequency + np.pi) * (1 - mutation)

    # Aura field
    aura_radius = 1.2 + 0.6 * frequency + 0.3 * np.sin(frame * frequency)
    X = aura_radius * np.cos(TH)
    Y = aura_radius * np.sin(TH)
    Z = T

    # Draw aura
    ax.plot_surface(X, Y, Z, color=color, alpha=0.25)

    # Draw DNA
    ax.plot(x1, y1, z, color='white', linewidth=2)
    ax.plot(x2, y2, z, color='white', linewidth=2)

    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_zlim(0, 4*np.pi)

    ax.set_title(
        f"EXTREME MODE | Chakra: {name}",
        color=color,
        fontsize=12
    )

ani = FuncAnimation(fig, update, interval=50)
plt.show()
