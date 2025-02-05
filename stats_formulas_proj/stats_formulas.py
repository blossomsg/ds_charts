import math
from collections import Counter

from typing import List

from vec_forumlas_proj.vec_formulas import sum_of_squares

num_friends = [100, 49, 41, 40, 25, 36, 96, 61, 89, 73, 55, 1, 2, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3]
cars_parked_different_areas = [55, 67, 43, 8, 57, 23, 15]
cars_parked_different_areas_even = [55, 67, 43, 8, 57, 23, 15, 87]
some_data = [19, 27, 15, 21, 33, 45, 7, 12, 20, 26]
some_data_2 = [575, 609, 335, 280, 729, 544, 852, 427, 967, 250]
some_data_3 = [15, 20, 21, 12, 17, 10]
some_data_4 = [10, 13, 17, 20, 23]  # -6.6, -3.6, 0.4, 3.4, 6.4


# Central Tendencies/ Measure of Central Tendency(terminology) was introduced in Std 9th - HSC
def mean(x_items: List[float]) -> float:
    """To get the average(mean) of the numerical data.
    Statistics was introduced as last chapter in the 7th class in SSC.
    You can find the examples in the book, but not the terminology.
    Statistics was repeated once again as chapter 11 in 8th class of SSC
    That is where they introduced "arithmetic mean or mean".
    """
    return sum(x_items) / len(x_items)


def _median_odd(x_items: List[float]) -> float:
    """If len(x_items) is odd, it's the average of the middle two elements"""
    return sorted(x_items)[
        len(x_items) // 2]  # the floor division // rounds the result down to the nearest whole number


def _median_even(x_items: List[float]) -> float:
    """If len(x_items) is even, it's the average of the middle two elements."""
    sorted_x_items = sorted(x_items)
    hi_midpoint = len(x_items) // 2  # len of items, floor division by 2, which results in a round off of quotient.
    return (sorted_x_items[hi_midpoint - 1] + sorted_x_items[hi_midpoint]) / 2  # median even formula


def median(x_items: List[float]) -> float:
    """Finds the 'middle most' value of x_items
    This topic is explained thoroughly well with an example chap 7 in std 9th SSC math part 1.
    """
    return _median_even(x_items) if len(x_items) % 2 == 0 else _median_odd(x_items)


# I am not sure about this topic since I have not noticed in any of the hsc books
def quantile(x_items: List[float], p: float) -> float:
    """Returns the p-th percentile value in x"""
    p_index = int(p * len(x_items))
    return sorted(x_items)[p_index]


def mode(x_items: List[float]) -> List[float]:
    """Returns a list, since there might be more than one mode.
    This topic is explained thoroughly well with an example chap 7 in std 9th SSC math part 1.
    """
    counts = Counter(x_items)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


"""
This topic is explained in the math - 1, std 11th chapter 8 - Measures of Dispersion  
Measures of Central Tendency mean, median, and mode gives the average but does not 
give any information about the spread of the data. The degree to which numerical data 
tend to spread about an average value is the variation or dispersion of the data.


Measures of dispersion commonly used:
Range - used in case of stock markets, and mean temperature of a certain place.
Variance
Standard deviation
"""


def data_range(x_item: List[float]) -> float:
    """Range is the simplest measure of dispersion. It is
    defined as difference between the largest value and
    the smallest value in the data.
    """
    return max(x_item) - min(x_item)


def de_mean(x_item: List[float]) -> List[float]:
    """Translate x_item by subtracting its mean(so the result has mean 0"""
    x_bar = mean(x_item)
    return [x - x_bar for x in x_item]


def variance(x_item: List[float]) -> float:
    """Almost the average squared deviation from the mean"""
    assert len(x_item) >= 2, "variance requires at least two elements"
    n = len(x_item)
    deviations = de_mean(x_item)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x_item: List[float]) -> float:
    """The standard deviation is the square root of the variance"""
    return math.sqrt(variance(x_item))


""" 
Topic Highlight in Data Science from scratch - Chapter 5 Statistics - covariance and correlation.

This topic is explained in the math - 2, std 12th chapter 3 - Linear Regression  
Correlation is used to measure the strength and direction of association between 2 variables.

Correlation coefficient measures association between 2 variables but cannot determine 
the value of one variable when the value of the other variable is known or given.
The technique used for predicting the value of one variable for a given value of the other
variable is called regression. Regression is a statistical tool for investigating the relationship
between variables. 
NOTE: Karl Pearson defined the coefficient of correlation known as Pearson’s
Product Moment correlation coefficient.

Note: Some statistical methods attempt to determine the value of an unknown quantity,
which may be a parameter or a random variable. The method used for this purpose is
called estimation if the unknown quantity is a parameter, and prediction if the unknown
quantity is a variable.

Linear Regression
Linear regression is a method of predicting the value of one variable when the values of
all other variables are known or specified. - 
Read 3.1 from Commerce Math - 2 - alot of jargons and explanations.

"""

if __name__ == "__main__":
    assert mean(num_friends) == 28.708333333333332
    assert median(cars_parked_different_areas) == 43.0
    assert median(cars_parked_different_areas_even) == 49.0
    assert quantile(cars_parked_different_areas, 0.10) == 8
    assert quantile(cars_parked_different_areas, 0.25) == 15
    assert quantile(cars_parked_different_areas, 0.75) == 57
    assert quantile(cars_parked_different_areas, 0.90) == 67
    assert set(mode(num_friends)) == {1, 2}
    assert data_range(cars_parked_different_areas) == 59
    assert variance(some_data_4) == 27.299999999999997
    assert standard_deviation(some_data_4) == 5.224940191045253


