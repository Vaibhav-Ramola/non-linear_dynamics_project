import numpy as np
import matplotlib.pyplot as plt
# from shapely.geometry import LineString # **** Import if only using Shapely



fig, axs = plt.subplots()           # Declaring the figure and axes


def findIntersectionPoints(f, g):
    # ***** Implementation using shapely library *****

    # first_string = LineString(np.column_stack((x, f)))
    # second_string = LineString(np.column_stack((x, g)))
    # intersection_points = first_string.intersection(second_string)
    
    # ***** Implementation using shapely library *****

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
max_of_x_dot = np.amax(np.absolute(x_dot))

y_axis = np.arange(-max_of_x_dot, max_of_x_dot, 0.001)         # y-axis is defined here

axs.plot(np.zeros(y_axis.shape), y_axis, '--k')                # plotting the y-axis with dashed line{'--'} and black color{'k'}
axs.plot(x, np.zeros(x.shape), '--k')                          # plotting the x-axis with dashed line{'--'} and black color{'k'}
#  **********     check 'fmt' string arguments for customizing plots in matplotlib     **********

axs.plot(x, x_dot, "-b")        #   plotting the x_dot v/s x variation in blue color

#       ********** Code below is used to annotate the graphs check Axis.annotate in matplotlib docs       ********** 

# To add arrowhead on the top of y-axis
axs.annotate("", 
    xy=(0, max_of_x_dot), 
    xytext=(0, max_of_x_dot+0.01), 
    arrowprops=dict(facecolor='black', 
    arrowstyle='<-'))

# To add arrowhead on the bottom of y-axis 
axs.annotate("", 
    xy=(0, -max_of_x_dot), 
    xytext=(0, -max_of_x_dot-0.01), 
    arrowprops=dict(facecolor='black', 
    arrowstyle='<-'))

# To add arrowhead to the right of x-axis
axs.annotate("", 
    xy=(np.max(x), 0), 
    xytext=(np.max(x)+1, 0), 
    arrowprops=dict(facecolor='black', 
    arrowstyle='<-'))

# To add arrowhead to the left of x-axis
axs.annotate("", 
    xy=(-np.max(x), 0), 
    xytext=(-np.max(x)-1, 0), 
    arrowprops=dict(facecolor='black', 
    arrowstyle='<-'))

# Setting the labels for the axis
axs.set_xlabel("x", fontsize= 20)         # Setting the x_label as "x"
axs.set_ylabel("x_dot", fontsize=20)      # Setting the y_label as "x_dot"

index = findIntersectionPoints(x_dot, np.array([0]*len(x)))  # function to find the indices of the intersection points of x_dot and x
plotStableUnstable(indexArray=index)                         # function to plot stable and unstable points in the graph

# *********** Implementation using shapely library **************

# plt.plot(x[index], x_dot[index], 'ro')

# intersections = findIntersectionPoints(x_dot, np.array([0] * len(x)), x)

# if intersections.geom_type == 'Multipoint':
#     axs.plot(*LineString(intersections).xy, 'ob')
# elif intersections.geom_type == 'Point':
#     axs.plot(*intersections.xy, 'ob')

# *********** Implementation using shapely library **************

axs.grid(True)              # function to display grid on the plot
axs.legend()                # function to show legends on the plot
plt.tight_layout()          # function to remove extra padding around the plot
plt.show()                  # function to show the plot