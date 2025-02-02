from typing import List, Tuple, Callable

Matrix = List[List[float]]
Vector = List[float]


# a = [[1, 2, 3],  # a has 2 rows and 3 columns
#      [4, 5, 6]]
#
# b = [[1, 2],  # B has 3 rows and 2 columns
#      [3, 4],
#      [5, 6]]


def shape(a: Matrix) -> Tuple[int, int]:
    """Returns (# of rows of A, # of columns of A"""
    num_rows = len(a)
    num_cols = len(a[0]) if a else 0
    return num_rows, num_cols


def get_row(a: Matrix, i: int) -> Vector:
    """Return the i-th row of A(as a Vector)"""
    return a[i]  # A[i] is already the ith row


def get_column(a: Matrix, j: int) -> Vector:
    """Return the i-th row of A(as a Vector)"""
    return [a_i[j] for a_i in a]  # jth element of row A_i, for each row A_i


# Callable needs a function to work and it returns float
def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]  ) -> Matrix:
    """Returns a num_rows x num_cols matrix whose (i, j)-th entry is entry_fn(i,j)"""
    # given i, create a list, [entry_fn(i, 0), ...], create one list for each i
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix
    Unit or
    This formula is mentioned in 11th HSC Math-1 book
    Determinants and Matrices - 4.4 - Introduction to Matrices -
    7 Unit or Identity Matrix
    Ex. i
    I3 = [1 0 0
          0 1 0
          0 0 1]
    """
    # for reference - the i row and j col range is calculated until they both are equal
    # eg: it first compares 0, 0 so we get 1 at first row, 1, 0 so we get 0 in second position and so on
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


if __name__ == "__main__":
    assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)  # 2 rows, 3 columns
    assert (get_row([[1, 2, 3], [4, 5, 6], [10, 2, 35]], 2)) == [10, 2, 35]
    assert get_column([[1, 2, 3], [4, 5, 6], [10, 2, 35]], 2) == [3, 6, 35]
    assert identity_matrix(5) == [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
