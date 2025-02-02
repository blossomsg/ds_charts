from __future__ import print_function

from typing import Tuple, Callable
from matrix_formulas_proj.matrix_forumlas import Matrix
from vec_forumlas_proj.vec_formulas import vector_sum, scalar_multiply

n1 = [2, 5, 6]
n2 = [5, 4, 2]
# print(len(n1) == len(n2))
# print(sum(v_i * w_i for v_i, w_i in zip(n1, n2)))

# print(magnitude_of_sum_of_squares([2, 4, 7]))

m = [[2, 5, 6], [5, 4, 2], [9, 6, 2]]


def shape(a: Matrix) -> Tuple[int, int]:
    """Returns (# of rows of A, # of columns of A"""
    num_rows = len(a)
    num_cols = len(a[0]) if a else 0
    return num_rows, num_cols


def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]) -> Matrix:
    """Returns a num_rows x num_cols matrix whose (i, j)-th entry is entry_fn(i,j)"""
    # given i, create a list, [entry_fn(i, 0), ...], create one list for each i
    return [[entry_fn(i, j) for j in range(num_cols) for i in range(num_rows)]]


def id_matrix(i: int, j: int):
    if i == j:
        print(i == j)
        print(1)
    else:
        print(0)


i = 3
j = 3
# v = [[id_matrix(ii, jj) for jj in range(j)] for ii in range(i)]
v = [[print(jj, ii) for jj in range(j)] for ii in range(i)]
print(v)


def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)
