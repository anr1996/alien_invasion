import matplotlib.pyplot as plt 

""" plt.style.use('seaborn')
fig, ax = plt.subplots()

# x and y values for the scatter plot.
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

ax.scatter(x_values,y_values, s=100)

# set the chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize =14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show() """


####################################

""" plt.style.use('seaborn')
fig, ax = plt.subplots()

# x and y values for the scatter plot.
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


ax.scatter(x_values,y_values, s=10)

# set the chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize =14)
ax.axis([0, 1100, 0, 1100000])

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()  """



""" plt.style.use('seaborn')
fig, ax = plt.subplots()

# x and y values for the scatter plot.
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# passing color red to graph line.
"""" ax.scatter(x_values,y_values,c='red', s=10) """"

# passing color light green to graph line.
ax.scatter(x_values,y_values,c=(0,0.8,0), s=10)

# set the chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize =14)
ax.axis([0, 1100, 0, 1100000])

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show() 
 """


plt.style.use('seaborn')
fig, ax = plt.subplots()

# x and y values for the scatter plot.
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

ax.scatter(x_values, y_values, c=(0, .8, 0), s=10)

# set the chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize =14)
ax.axis([0, 1100, 0, 1100000])

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('squares_plot.png',bbox_inches='tight')