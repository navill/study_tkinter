import itertools

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)  # x축 값
line, = ax.plot(x, np.sin(x))  # sin(y 축)


def data_gen():
    for i in range(0, 999999):
        yield i


def animate(data):
    line.set_ydata(np.sin(x + data / 50))  # update the data.
    return line,


ani = animation.FuncAnimation(fig=fig, func=animate, frames=data_gen, interval=20, save_count=50)


plt.show()
