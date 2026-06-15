import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
start = -100
stop = 100
num = 100

x1 = np.linspace(start, stop, num)


step_size = (stop-start)/(num -1)

x1_values = []
y_values = []


for i in range(num):
    x1 = -100 + (i * step_size)

    y = 2 * x1 + 3

x1_values.append(x1)
y_values.append(y)


plt.plot(x1_values, y_values, label="y = 2x1 + 3", color="red", linewidth=2)

# to set a text headline at the very top of your chart.
plt.title("Plot using Python For Loop")
plt.xlabel("x1")
plt.ylabel("y")

plt.axhline(0, color="black", linewidth=0.5, linestyle="--")

plt.axvline(0, color="black", linewidth=0.5, linestyle="--")

plt.grid(True)

plt.legend()
plt.show()