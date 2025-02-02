import math
from typing import List

Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements.
    ->a+->b (a and b vector quantity, -> = direction)
    This formula is mentioned in 12th HSC Math-1 book
    Vectors - 5.1.4 - Addition of Two Vectors
    Ex. 10 - ii
    ->a=4i+3k and ->b = 2i+j+5k
    ->a+->b =(4i+0j+3k)+(-2i+j+5k) = (4i+(-2i))+(0j+1j)+(3k+5k) = 2i+j+8k
    """
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements.
    ->a-->b (a and b vector quantity, -> = direction)
    This formula is mentioned in 12th HSC Math-1 book
    Vectors - 5.1.5 - Subtraction of Two Vectors
    Ex. 10 - ii
    ->a=4i+3k and ->b = 2i+j+5k
    ->a-->b =(4i+0j+3k)-(-2i+j+5k) = (4i-(-2i))-(0j-j)+(3k+5k) = 6i-j-2k
    """
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements."""
    # Check that vectors are not empty
    assert vectors, "no vectors provided!"

    # Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    # the i-th element of the result in the sum of every vector[i]
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every element by c.
    2->a (a vector quantity, -> = direction) (->a be any vector, k be a scalar = |ka|)
    This formula is mentioned in 12th HSC Math-1 book
    Vectors - 5.1.3 - Scalar Multiplication
    Ex. 10 - iv
    3b = 3(-2i+j+5k) = -6k+3j+15k
    """
    return [c * v_i for v_i in v]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1+......v_n * w_n
    ->a.->b(a.b dot product/scalar product)
    This formula is mentioned in 12th HSC Math-1 book
    Vectors - 5.3.1 - Scalar Product of 2 vectors - definition
    Vectors - 5.3.2 - Finding angle between 2 vectors
    Note: 4
    a.b = (a1i+a2j+a3k).(b1i+b2j+b3k) = a1b1+a2b2+a3b3
    """
    assert len(v) == len(w), "vectors must be same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n
    This formula is first part of the formula mentioned
    in 12th HSC Math-1 book.
    Vectors - 5.1.10 - Position vector of a point P(x, y, z) in space
    Ex. 3 - i and ii
    i: a = i-2j-4k -> |a| = math.sqrt(1^2+(-2)^2+4^2 or 1**2+(-2)**2+4**2)
    """
    return dot(v, v)


def magnitude_of_squares(v: Vector) -> float:
    """Returns magnitude of sum of squares.
    This formula is second part mentioned in 12th HSC Math-1 book
    Vectors - 5.1.10 - Position vector of a point P(x, y, z) in space
    Ex. 3 - i and ii
    i: a = i-2j-4k -> |a| = math.sqrt(1^2+(-2)^2+4^2 or 1**2+(-2)**2+4**2)
    """
    return math.sqrt(sum_of_squares(v))

def squared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n)**2
    This formula is first part mentioned in 12th HSC Math-1 book
    Vectors - 5.1.8 - 3-D coordinate system
    Topic - Distance between any two points in space
    Ex. 11 - d
    point (2,3,4) and (-2, 7, 3)
    math.sqrt(2+2)**2 + (3-7)**2 + (4-3)**2
    """
    return sum_of_squares((subtract(v, w)))

def distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n)**2
    This formula is first part mentioned in 12th HSC Math-1 book
    Vectors - 5.1.8 - 3-D coordinate system
    Topic - Distance between any two points in space
    Ex. 11 - d
    point (2,3,4) and (-2, 7, 3)
    math.sqrt(2+2)**2 + (3-7)**2 + (4-3)**2
    """
    return math.sqrt(squared_distance(v, w))


if __name__ == "__main__":
    # Addition of 2 vectors
    assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9], "LHS != RHS"
    # Subtraction of 2 vectors
    assert subtract([1, 2, 3], [4, 5, 6]) == [-3, -3, -3], "LHS != RHS"
    assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3], "LHS != RHS"
    # Sum of Vectors
    assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20], "LHS != RHS, sum of all vectors"
    # Scalar Multiplication
    assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]
    # Element-wise average
    assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]
    # Scalar Dot Product
    assert dot([1, 2, 3], [4, 5, 6]) == 32
    # Part 1 Sum of the squared numbers
    assert sum_of_squares([2, 4, 7]) == 69
    # Magnitude of sum of squares
    assert magnitude_of_squares([2, 4, 7]) == 8.306623862918075
