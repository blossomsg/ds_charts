from operator import index

import numpy as np
import pandas as pd

"""
reindex, which means to create a new object with the values rearranged to align with the new index.
"""

# eg: 1
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=["d", "b", "a", "c"])
# print(obj)
obj2 = obj.reindex(["a", "b", "b", "d", "e"])
# print(obj2)

# eg: 2
obj3 = pd.Series(["blue", "purple", "yellow"], index=[0, 5, 9])
# print(obj3)
# print(obj3.reindex(np.arange(15), method="ffill"))
frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=["a", "c", "d"], columns=["Maharashtra", "Goa", "Bihar"])
# print(frame)

# eg: 3
frame2 = frame.reindex(index=["a", "b", "c", "d"])
# print(frame2)

# eg: 4 - not sure what is happening here
states = ["Maharashtra", "Goa", "Bihar"]
# print(frame.reindex(columns=states))

# eg: 5
# print(frame.loc[["a", "d", "c"], ["Maharashtra", "Goa"]])


# eg: 6
obj4 = pd.Series(np.arange(5.), index=["a", "b", "c", "d", "e"])
# print(obj4)

# eg: 7
new_obj = obj4.drop("c")
# print(new_obj)

# eg: 8
# print(obj4.drop(["d", "c"]))

data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=["Maharashtra", "Goa", "Bihar", "AndraPradesh"],
                    columns=["one", "two", "three", "four"])

""" drop data axis=1 is for columns and axis=0 is for rows"""
# print(data)
# print(data.drop(index=["Maharashtra", "Bihar"]))
# print(data.drop(columns=["two"]))
# print(data.drop(["two", "three"], axis=1))
# print(data.drop(["two", "three"], axis="columns"))

# eg: 9
obj5 = pd.Series(np.arange(4.), index=["a", "b", "c", "d"])
# print(obj5["b"])
# print(obj5[1])
# print(obj5[2:4])
# print(obj5[["b", "a", "d"]])
# print(obj5 < 2)

# eg: 10
obj6 = pd.Series([1, 2, 3], index=[2, 0, 1])
obj7 = pd.Series([1, 2, 3], index=["a", "b", "c"])
obj8 = pd.Series(["d", "e", "f"], index=["a", "b", "c"])
# print(obj6)
# print(obj7)
# print(obj8)
"""loc Index should have integers"""
# print(obj7.loc[[0, 1]])
"""Since loc operator indexes exclusively with labels, there is also an iloc operator
that indexes exclusively with integers to work consistently whether or not the index
contains integers
axis labels(index values)
"""
# print(obj6.iloc[[0, 1]])

# eg: 11
# Indexing
# print(data[1:3])

# eg: 12
# print(data.loc["Goa"])
# print(data.loc["Goa", ["two", "three"]])
