import numpy as np
from matplotlib import pyplot as plt

capital_cr = np.array([2, 3, 4, 5, 6, 8, 9])
profit_lakh = np.array([6, 5, 7, 7, 8, 9, 10])

# Fit a line of the best fit
slope, intercept = np.polyfit(capital_cr, profit_lakh, 1)
y_fit = slope * capital_cr + intercept

r = np.corrcoef(capital_cr, profit_lakh)[0, 1]
plt.figure()
plt.scatter(capital_cr, profit_lakh, color="blue", label="Data Points")
plt.plot(capital_cr, y_fit, color="red", label="Best Fit line")
plt.xlabel("Capital in corers")
plt.ylabel("Profits in lakhs")
plt.title("Scatter Diagram: Capital vs Profit")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

print(f"Correlation coefficient (r): {r:.3f}")


# import numpy as np
# from matplotlib import pyplot as plt
#
# capital_cr = np.array([10, 20, 30, 40, 50, 60, 70])
# profit_lakh = np.array([30, 20, 24, 36, 40, 28, 38])
#
# # Fit a line of the best fit
# slope, intercept = np.polyfit(capital_cr, profit_lakh, 1)
# y_fit = slope * capital_cr + intercept
#
# r = np.corrcoef(capital_cr, profit_lakh)[0, 1]
# plt.figure()
# plt.scatter(capital_cr, profit_lakh, color="blue", label="Data Points")
# plt.plot(capital_cr, y_fit, color="red", label="Best Fit line")
# plt.xlabel("Capital in corers")
# plt.ylabel("Profits in lakhs")
# plt.title("Scatter Diagram: Capital vs Profit")
# plt.legend()
# plt.grid()
# plt.tight_layout()
# plt.show()
#
# print(f"Correlation coefficient (r): {r:.3f}")