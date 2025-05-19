import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.animation as animation


# === define the lorenz system ===
# x, y, and z make up the system state
# t is time,
# sigma, rho, beta are the system parameters
def lorenz_system(current_state, t):
    x, y, z = current_state

    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z

    return [dx_dt, dy_dt, dz_dt]


# define the initial system state, system parameters
initial_state = [-0.1, 0.01, 0.08]
sigma = 10.
rho = 50.
beta = 3.

start_time = 0
end_time = 10
num_points = 100 * (end_time - start_time)
time_points = np.linspace(start_time, end_time, num_points)

# === generate datas =========
xyz = odeint(lorenz_system, initial_state, time_points)
data = np.array(xyz).T * 0.01  # scale down to 0.01
print(data)

print(data[0])


# === 2d plot lorenz ====
def lorenz_2d_plot(data):
    fig, axs = plt.subplots(3, 1, sharex='all')

    xxx = range(len(data[2]))
    axs[2].set_xlim(0, 1000)
    axs[2].set_xlabel('time')

    axs[0].plot(xxx, data[0], color='r', alpha=0.7, linewidth=0.7)
    axs[0].set_ylabel('x')

    axs[1].plot(xxx, data[1], color='g', alpha=0.7, linewidth=0.7)
    axs[1].set_ylabel('y')

    axs[2].plot(xxx, data[2], color='b', alpha=0.7, linewidth=0.7)
    axs[2].set_ylabel('z')

    fig.tight_layout()
    fig.savefig('matplotlib_lorenz-2d.png', dpi=300, bbox_inches='tight')
    plt.show()


lorenz_2d_plot(data)


# === 3d plot lorenz ====
def lorenz_3d_plot(data):
    fig = plt.figure()
    ax = Axes3D(fig)

    ax.xaxis.set_pane_color((1, 1, 1, 1))
    ax.yaxis.set_pane_color((1, 1, 1, 1))
    ax.zaxis.set_pane_color((1, 1, 1, 1))

    ax.set_title('Lorenz')

    ax.set_xlim3d([-0.5, 0.5]), ax.set_xlabel('X')
    ax.set_ylim3d([-0.5, 0.5]), ax.set_ylabel('Y')
    ax.set_zlim3d([0.0, 1.0]), ax.set_zlabel('Z')

    # ax.view_init(30, -60)               # default view

    ax.plot(data[0], data[1], data[2], color='r', alpha=0.7, linewidth=0.75)
    ax.set_title('Lorenz_3d')

    fig.savefig('matplotlib_lorenz-3d.png', dpi=300, bbox_inches='tight')
    plt.show()


lorenz_3d_plot(data)


# === 3d plot lorenz ====
def lorenz_3d_plot_ani(data):
    fig = plt.figure()
    ax = Axes3D(fig)

    ax.xaxis.set_pane_color((1, 1, 1, 1))
    ax.yaxis.set_pane_color((1, 1, 1, 1))
    ax.zaxis.set_pane_color((1, 1, 1, 1))

    ax.set_title('Lorenz_3d_animation')

    ax.set_xlim3d([-0.5, 0.5]), ax.set_xlabel('X')
    ax.set_ylim3d([-0.5, 0.5]), ax.set_ylabel('Y')
    ax.set_zlim3d([0.0, 1.0]), ax.set_zlabel('Z')

    # ax.view_init(30, -60)               # default view

    # === Animation Functions ===
    def update_line(num, data, line):
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
        return line

    # initial with the start point
    line, = ax.plot(data[0][0:1], data[1][0:1], data[2][0:1], color='r', alpha=0.7, linewidth=0.75)
    ani = animation.FuncAnimation(fig, update_line, 1000, fargs=(data, line), interval=1)

    # ani.save('matplotlib_lorenz_3d_ani.mp4', fps=24, dpi=300)
    ani.save('03_lorenz_3d_ani.gif')
    plt.show()


lorenz_3d_plot_ani(data)
