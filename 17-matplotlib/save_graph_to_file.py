import matplotlib.pyplot as pyplot

# Plot a sequence of values
pyplot.plot([3, 4, 6, 9, 11, 12, 10, 11, 14, 16])

print('Saving plot as png file')

# Save the plot to a file
pyplot.savefig('plot.png')
