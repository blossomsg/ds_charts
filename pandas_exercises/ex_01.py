import numpy as np
import pandas as pd

"""
Series
A Series is a one-dimensional array-like object containing a sequence of values 
of the same type and an associated array of data labels, called its index. The 
simplest Series is formed from only an array of data.

Another way to think about a Series is as a fixed-length, ordered dictionary, as it is a
mapping of index values to data values. It can be used in many contexts where you
might use a dictionary.
"""
# eg: 1
obj = pd.Series([4, 7, -5, 3])
# print(obj)

# Output
# 0    4
# 1    7
# 2   -5
# 3    3
# dtype: int64

# eg: 2
obj2 = pd.Series([4, 7, -5, 3], index=["d", "b", "a", "c"])
# print(obj2.index)
# print(obj2["a"])
# print(obj2 > 0)
# print(obj2[obj2 > 0])
# print(obj2 * 2)

# eg: 3
sdata = {"Maharashtra": 35000, "AndraPradesh": 71000, "UttarPradesh": 16000, "Amboli": 5000}
obj3 = pd.Series(sdata)
# print(obj3)
# print(obj3.to_dict())

# eg: 4
states = ["Maharashtra", "AndraPradesh", "UttarPradesh", "Goa"]
obj4 = pd.Series(sdata, index=states)
# print(obj4)
# print(obj4.isna()) # to get bool status for NaN
# print(obj4.notna()) # to get bool status for not NaN

# eg: 5
# arithmetic operations
# print(obj3 + obj4)

# eg: 6
obj4.name = "polulation"
obj4.index.name = "state"
# print(obj4)

# eg: 7
# print(obj)
obj.index = ["Bob", "Steve", "Jeff", "Ryan"]
# print(obj)

"""
DataFrame
A DataFrame represents a rectangular table of data and contains an ordered, named
collection of columns, each of which can be a different value type (numeric, string,
Boolean, etc.). The DataFrame has both a row and column index; it can be thought of
as a dictionary of Series all sharing the same index.
"""

# eg: 8
data = {"state": ["Maharashtra", "Maharashtra", "Maharashtra", "Goa", "Goa", "Goa"],
        "year": [2000, 2001, 2002, 2000, 2001, 2002], "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
# print(frame)
# print(frame.head())  # prints first 5
# print(frame.tail())  # prints last 5

# eg: 9
# print(pd.DataFrame(data, columns=["year", "state", "pop"]))

# eg: 10
frame2 = (pd.DataFrame(data, columns=["year", "state", "pop", "debt"]))
# print(frame2)  # if data is missing a dict key it will show NaN

# eg: 11
# print(frame2.columns)
# print(frame2.year)
# print(frame2.state)

# eg: 12
# print(frame2.loc[1])
# print(frame2.iloc[2])

# eg: 13
frame2["debt"] = 16.5
# print(frame2)
frame2["debt"] = np.arange(6.)
# print(frame2)

# eg: 14
frame2["eastern"] = frame2["state"] == "Goa"
# print(frame2)

# eg: 15
del frame2["eastern"]
# print(frame2.columns)

# eg: 16
populations = {"Goa": {2000: 1.5, 2001: 1.7, 2002: 3.6}, "Maharashtra": {2001: 2.4, 2002: 2.9}}
frame3 = pd.DataFrame(populations)
# print(frame3)
# print(frame3.T)  # Transposing/swap rows and columns

# eg: 17
# print(pd.DataFrame(populations, index=[2000, 2001, 2002]))

# eg: 18
pdata = {"Maharashtra": frame3["Maharashtra"][:-1], "Goa": frame3["Goa"][:2]}
# print(pd.DataFrame(pdata))

# eg: 19
# print(frame3.to_numpy())

"""
Index Objects
pandas’s Index objects are responsible for holding the axis labels (including a Data‐
Frame’s column names) and other metadata (like the axis name or names). Any array
or other sequence of labels you use when constructing a Series or DataFrame is
internally converted to an Index
"""
# eg: 20
obj5 = pd.Series(np.arange(3), index=["a", "b", "c"])
index = obj5.index
# print(index[1:])

# eg: 21
# index[1] = "d"  # TypeError

# eg: 22
labels = pd.Index(np.arange(3))
# print(labels)
obj6 = pd.Series([1.5, -2.5, 0], index=labels)
# print(obj6)
# print(obj6.index is labels)

# eg: 23
# print(frame3)
# print(frame3.columns)
# print("Goa" in frame3.index)

# eg: 24
# print(pd.Index(["foo", "foo", "bar", "bar"]))

