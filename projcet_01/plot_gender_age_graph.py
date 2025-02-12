from matplotlib import pyplot as plt

from projcet_01.creating_database import df

# Plotting graph - Gender Colors with Age group
colors_labels = ("blue", "green")
gender_labels = ("Male", "Female")

# unstack type
# https://naomi-fridman.medium.com/pandas-groupby-explained-with-titanic-6a1c47eb8182
gender_counts = df[["Age", "Gender"]].replace((0, 1), gender_labels)
# Joint Bar graph for Gender
gender_counts.groupby(["Age", "Gender"])["Gender"].count().unstack().plot.bar(title="Joint Bar Graph", figsize=(8, 6),
                                                                              color=("blue", "red"),
                                                                              ylabel="Total Gender Count")
# Sub-divided bar graph for Gender
gender_counts.groupby(["Age", "Gender"])["Gender"].count().unstack().plot.bar(title="Sub-divided Bar Graph",
                                                                              stacked=True, figsize=(8, 6),
                                                                              color=("blue", "red"),
                                                                              ylabel="Total Gender Count")
print(gender_counts.value_counts())
plt.show()
