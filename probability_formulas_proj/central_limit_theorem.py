import math
from collections import Counter
from random import random

import matplotlib.pyplot as plt

from probability_formulas_proj.normal_cdfs_formula import normal_cdf


def bernoulli_trial(p: float) -> int:
    """Return 1 with probability p and 0 with probability 1-p"""
    return 1 if random() < p else 0


def binominal(n: int, p: float) -> int:
    """Returns the sum of n bernoulli(p) trials"""
    return sum(bernoulli_trial(p) for _ in range(n))


def binominal_histogram(p: float, n: int, num_points: int) -> None:
    """Picks points from a binomial(n, p) and plots their histogram"""
    data = [binominal(n, p) for _ in range(num_points)]

    # use a bar chart to show the actual binominal samples
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()], [v / num_points for v in histogram.values()], 0.8, color='0.75')
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # use a line chart to show the normal approximation
    x_item = range(min(data), max(data) + 1)
    y_item = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) for i in x_item]
    plt.plot(x_item, y_item)
    plt.title("Biominal Distribution vs. Normal Approximation")
    plt.show()

if __name__ == "__main__":
    binominal_histogram(0.75, 100, 10000)
