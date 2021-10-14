import matplotlib.pyplot as pyplot

labels = ('Python', 'Java', 'Scala', 'C#')
sizes = [45, 30, 15, 10]

pyplot.pie(sizes,
           labels=labels,
           autopct='%.1f%%', # display the percentage value to 1 decimal place
           counterclock=False,
           startangle=90)

pyplot.show()
