import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import LineString


def findIntersectionPoints(f, g, x):
    first_string = LineString(np.column_stack((x, f)))
    second_string = LineString(np.column_stack((x, g)))
    intersection_points = first_string.intersection(second_string)

    return intersection_points


x1 = eval(input("x1 : "))
x2 = eval(input("x2 : "))

x = np.arange(x1, x2, 0.001)
x_dot = eval(input("x_dot : "))
y_axis = np.arange(-np.max(np.abs(x_dot)), np.max(np.abs(x_dot)))

fig, axs = plt.subplots()

axs.plot(np.zeros(y_axis.shape), y_axis, '--k')
axs.plot(x, np.zeros(x.shape), '--k')
axs.plot(x, x_dot, "-b")

axs.annotate("x_dot", xy=(0, np.max(x_dot)), xytext=(0, np.max(x_dot)+2), arrowprops=dict(facecolor='black', arrowstyle='<-'))
axs.annotate("", xy=(0, -np.max(x_dot)), xytext=(0, -np.max(x_dot)-2), arrowprops=dict(facecolor='black', arrowstyle='<-'))
axs.annotate("x", xy=(np.max(x), 0), xytext=(np.max(x)+2, 0), arrowprops=dict(facecolor='black', arrowstyle='<-'))
axs.annotate("", xy=(-np.max(x), 0), xytext=(-np.max(x)-2, 0), arrowprops=dict(facecolor='black', arrowstyle='<-'))

axs.set_xlabel("x")
axs.set_ylabel("x_dot")

intersections = findIntersectionPoints(x_dot, x, x)

print(intersections)

axs.grid(True)

plt.show()




