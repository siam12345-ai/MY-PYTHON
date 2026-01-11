import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Time
t = np.linspace(0, 4*np.pi, 300)
theta = np.linspace(0, 2*np.pi, 50)
T, TH = np.meshgrid(t, theta)

# Physics parameters
f = 0.06                  # chakra frequency
omega = 2 * np.pi * f     # angular frequency
k = 1                     # wave number
A0 = 1.2                  # base aura radius
v = 0.1                   # vertical growth

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def update(frame):
    ax.clear()
    time = frame * 0.05

    # Calculus-based mutation
    R = 1 + 0.3 * np.sin(omega * time)
    dR_dt = 0.3 * omega * np.cos(omega * time)

    # DNA helix
    x = R * np.cos(omega * t)
    y = R * np.sin(omega * t)
    z = v * t

    # Aura wave field
    aura = A0 + np.sin(k * T - omega * time)

    X = aura * np.cos(TH)
    Y = aura * np.sin(TH)
    Z = v * T

    ax.plot_surface(X, Y, Z, color='cyan', alpha=0.25)
    ax.plot(x, y, z, color='white', linewidth=2)

    ax.set_title(
        f"ω={omega:.2f} | dR/dt={dR_dt:.2f}",
        color='cyan'
    )

    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_zlim(0, 4)

ani = FuncAnimation(fig, update, interval=50)
plt.show()
