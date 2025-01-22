"""These are a good choice for showing trends"""
from matplotlib import pyplot

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

# We can make multiple calls to pyplot.plot
# to show multiple series on the same chart
pyplot.plot(xs, variance, "g-", label="variance")  # green solid line
pyplot.plot(xs, bias_squared, "r-", label="bias^2")  # red dot-dashed line
pyplot.plot(xs, total_error, "b:", label="total error")  # blue dotted line

# Because we've assigned labels to each series,
# We can get a legend for free (loc=9 means "top center")
pyplot.legend(loc=9)
pyplot.xlabel("model complexity")
pyplot.xticks([])
pyplot.title("The Bias-Variance Tradeoff")
pyplot.show()
