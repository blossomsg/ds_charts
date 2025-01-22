""" A bar chart is a good choice to show some quantity varies among some discrete set of items."""

from matplotlib import pyplot

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# plot bars with left x-coordinates [0, 1, 2, 3, 4], heights [num_oscars]
pyplot.bar(range(len(movies)), num_oscars)

pyplot.title("My Favorite Movies")
pyplot.ylabel("# of Academy Awards")

# label x-axis with movie names at bar centers
pyplot.xticks(range(len(movies)), movies)

pyplot.show()

