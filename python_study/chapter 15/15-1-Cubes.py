import matplotlib.pyplot as plt 

""" # x values in range of 1-5
x_values = range(1, 5)

# y values represented by x values cubed.
y_values = [x**3 for x in x_values] """

x_values = [1,5000]
y_values = [x**3 for x in x_values]

# graph background type.
plt.style.use('seaborn')
fig, ax = plt.subplots()

# scatter plot assigned x and y values.
ax.scatter(x_values, y_values, c=(1, 0.2, 1),s=10)

# title and font size
ax.set_title("square numbers", fontsize=24)

# x axis label and font size.
ax.set_xlabel("Value", fontsize=14)

# y axis label font size.
ax.set_ylabel("Square of Value", fontsize=14)

# plot line assign x and y values, line color and line width.
ax.plot(x_values, y_values,c=(1, 0.2, 1), linewidth=3)


# set of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# show graph visual.
plt.show()
