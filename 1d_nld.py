
from cProfile import label
from matplotlib import markers
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import LineString

def findIntersectionPoints(f, g, x):
    # first_string = LineString(np.column_stack((x, f)))
    # second_string = LineString(np.column_stack((x, g)))
    # intersection_points = first_string.intersection(second_string)
    idx = np.argwhere(np.diff(np.sign(f-g))).flatten()
    return idx

def plotStableUnstable(indexArray):
    for index in indexArray:
        if x_dot[index+1]>0 and x_dot[index-1]<0:
            axs.plot(x[index], x_dot[index], marker='o', markerfacecolor='none', markeredgecolor='blue', label="Stable Points")
        elif x_dot[index+1]<0 and x_dot[index-1]>0:
            axs.plot(x[index], x_dot[index], marker='o', markerfacecolor='blue', label="Unstable Points")
    


x1 = eval(input("x1 : "))
x2 = eval(input("x2 : "))

x = np.arange(x1, x2, 0.001)
x_dot = eval(input("x_dot : "))
y_axis = np.arange(-np.amax(np.absolute(x_dot)), np.amax(np.absolute(x_dot)), 0.001)

fig, axs = plt.subplots()

axs.plot(np.zeros(y_axis.shape), y_axis, '--k')
axs.plot(x, np.zeros(x.shape), '--k')
axs.plot(x, x_dot, "-b")

axs.annotate("", xy=(0, np.amax(np.absolute(x_dot))), xytext=(0, np.amax(np.absolute(x_dot))+0.01), arrowprops=dict(facecolor='black', arrowstyle='<-'))
axs.annotate("", xy=(0, -np.amax(np.absolute(x_dot))), xytext=(0, -np.amax(np.absolute(x_dot))-0.01), arrowprops=dict(facecolor='black', arrowstyle='<-'))
axs.annotate("", xy=(np.max(x), 0), xytext=(np.max(x)+1, 0), arrowprops=dict(facecolor='black', arrowstyle='<-'))
axs.annotate("", xy=(-np.max(x), 0), xytext=(-np.max(x)-1, 0), arrowprops=dict(facecolor='black', arrowstyle='<-'))

axs.set_xlabel("x")
axs.set_ylabel("x_dot")

index = findIntersectionPoints(x_dot, np.array([0]*len(x)), x)
plotStableUnstable(indexArray=index)

# plt.plot(x[index], x_dot[index], 'ro')

# intersections = findIntersectionPoints(x_dot, np.array([0] * len(x)), x)

# if intersections.geom_type == 'Multipoint':
#     axs.plot(*LineString(intersections).xy, 'ob')
# elif intersections.geom_type == 'Point':
#     axs.plot(*intersections.xy, 'ob')


axs.grid(True)
axs.legend()
plt.show()




