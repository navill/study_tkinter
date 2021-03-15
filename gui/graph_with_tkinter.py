import tkinter

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# animation + tkinter

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)  # x축 값
line, = ax.plot(x, np.sin(x))  # sin(y 축)


def data_gen():
    for i in range(0, 999999):
        yield i


def animate(data):
    # print(data)
    line.set_ydata(np.sin(x + data / 50))  # update the data.
    return line,


window = tkinter.Tk()  # 추가
label = tkinter.Label(window, text="라벨").grid(column=0, row=0)  # 추가
canvas = FigureCanvasTkAgg(fig, master=window)  #
canvas.get_tk_widget().grid(column=0, row=1)  #

anim = animation.FuncAnimation(fig=fig, func=animate, frames=data_gen, interval=50, save_count=50)
window.mainloop()
