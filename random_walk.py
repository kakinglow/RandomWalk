import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import random
import matplotlib.animation as animation
import numpy as np

def random_walk(n, dimensions):

    x_list, y_list = [], []
    position = [0, 0, 0]
    coord = []
    x, y = 0, 0
    if dimensions == 2:
        for i in range(n):
            (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            x += dx
            y += dy

            x_list.append(x)
            y_list.append(y)

        return x_list, y_list
    
    if dimensions == 3:
        for i in range(n):
            axis = random.randrange(0, 3)
            position[axis] += random.choice([-1, 1])
            coord.append(position[:])
            x, y, z = zip(*coord)
        return x, y, z

# 2d Random Walk Matplotlib

def update_2d(num, x, y, line):
        line.set_data(x[:num], y[:num])
        return line,

def graph_2d(x, y):
    fig, ax = plt.subplots()
    line, = ax.plot(x, y, color = "darkorchid")

    ani = animation.FuncAnimation(fig, update_2d, len(x), fargs=[x, y, line], interval=1, blit=True)

    plt.show()

# 3d Random Walk Matplotlib

def update_3d(num, x, y, z, line):
    line.set_data(x[:num], y[:num])
    line.set_3d_properties(z[:num])
    return line,


def graph_3d(x, y ,z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    line, = ax.plot(x, y, z, color = "darkorchid")

    ani = animation.FuncAnimation(fig, update_3d, len(x), fargs=[x, y, z, line], interval=1, blit=True)
    ani.save('3d_rw.gif', writer='imagemagick', fps=60)

    plt.show()

x, y, z = random_walk(500, 3)
graph_3d(x, y, z)





