import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation
import numpy as np

def random_walk(n, dimensions):

    x_list, y_list = [], []
    x, y = 0, 0
    if dimensions == 2:
        for i in range(n):
            (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            x += dx
            y += dy

            x_list.append(x)
            y_list.append(y)

        return x_list, y_list


x, y = random_walk(10000, 2)

fig, ax = plt.subplots()
line, = ax.plot(x, y, color = "darkorchid")

def update(num, x, y, line):
    line.set_data(x[:num], y[:num])
    return line,

ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, line], interval=1, blit=True, repeat=False)

plt.show()



