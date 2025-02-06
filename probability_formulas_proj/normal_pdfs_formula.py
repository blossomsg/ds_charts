import math

from matplotlib import pyplot as plt

from probability_formulas_proj.probability_formulas import SQRT_TWO_PI


def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma)


# Normal pdfs
x_item = [x / 10.0 for x in range(-50, 50)]
plt.plot(x_item, [normal_pdf(x, sigma=1) for x in x_item], '-', label='mu=0,sigma=1')
plt.plot(x_item, [normal_pdf(x, sigma=2) for x in x_item], '--', label='mu=0,sigma=2')
plt.plot(x_item, [normal_pdf(x, sigma=0.5) for x in x_item], ':', label='mu=0,sigma=0.5')
plt.plot(x_item, [normal_pdf(x, mu=-1) for x in x_item], '-.', label='mu=1,sigma=1')
plt.legend()
plt.title("Various Normal pdfs")

# Normal cdfs


if __name__ == "__main__":
    plt.show()
