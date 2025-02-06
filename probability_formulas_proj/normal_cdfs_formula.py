import math

import matplotlib.pyplot as plt


def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def inverse_normal_cdf(p: float, mu: float = 0, sigma: float = 1, tolerance: float = 0.00001) -> float:
    """find approx. inverse using binary search"""
    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z = -10.0
    hi_z = 10.0
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z = mid_z
        else:
            hi_z = mid_z

        return mid_z


x_item = [x / 10.0 for x in range(-50, 50)]
plt.plot(x_item, [normal_cdf(x, sigma=1) for x in x_item], '-', label='mu=0, sigma=1')
plt.plot(x_item, [normal_cdf(x, sigma=2) for x in x_item], '--', label='mu=0, sigma=2')
plt.plot(x_item, [normal_cdf(x, sigma=0.5) for x in x_item], ':', label='mu=0, sigma=0.5')
plt.plot(x_item, [normal_cdf(x, mu=-1) for x in x_item], '-.', label='mu=-1, sigma=1')
plt.legend(loc=4)  # bottom right
plt.title("Various Normal cdfs")
plt.show()

if __name__ == "__main__":
    plt.show()
