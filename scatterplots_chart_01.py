from matplotlib import pyplot

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

pyplot.scatter(friends, minutes)
# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    # Put the label with its point but slightly offset
    pyplot.annotate(label, xy=(friend_count, minute_count), xytext=(5, -5), textcoords="offset points")

pyplot.title("Daily Minutes vs. Number of Friends")
pyplot.xlabel("# of friends")
pyplot.ylabel("daily minutes spent on the site")
pyplot.show()
