from collections import Counter
from symbol import yield_expr

from matplotlib import pyplot

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Bucket grades by decile, but put 100 in with the 90's , floor division of grades(gives the first quotient number)
# Counter counts the number of items repeated in the list, maps the count to the items in the list
# print(min(grade // 10*10, 90) for grade in grades) - gives you the actual numbers
histo = Counter(min(grade // 10 * 10, 90) for grade in grades)
# print(histo)
# eg: Counter({80: 4, 90: 3, 70: 3, 0: 2, 60: 1})


# Shift bars right by 5, Give each bar its correct height, Give each bar a width of 10, Black edges for each bar.
pyplot.bar([x + 5 for x in histo.keys()], histo.values(), 10, edgecolor=(0, 0, 0))
# Below are the actual widths of the bar(less confusing).
# pyplot.bar([x + 5 for x in histo.keys()], histo.values(), edgecolor=(0, 0, 0))
# print([x + 5 for x in histo.keys()])

pyplot.axis([-5, 105, 0, 5])  # x-axis from -5 to 105, y-axis from 0 to 5

pyplot.xlabel("Decile")
pyplot.ylabel("# of Students")
pyplot.title("Distribution of Exam 1 Grades")
pyplot.show()
