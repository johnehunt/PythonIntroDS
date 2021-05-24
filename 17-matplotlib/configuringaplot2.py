import matplotlib
import matplotlib.pyplot as pyplot

x = range(1, 11)
y = [3, 4, 6, 9, 11, 12, 10, 11, 14, 16]

# Set the axes headings
pyplot.ylabel('y values', fontsize=12)
pyplot.xlabel('x values', fontsize=12)

# Set the title
pyplot.title("Sample Graph using MatPlotLib " + str(matplotlib.__version__))
# Configure line on plot
pyplot.plot(x, y, linewidth=2.0, label="samples", marker='o', color='blue', linestyle='--')

# Include a grid
pyplot.grid()

# Display the graph
pyplot.show()
