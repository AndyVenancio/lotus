import math 
import numpy as np
import matplotlib.pyplot as plt

data = [78.5, 76.5, 75.5, 75, 74.5, 73.5, 72.5, 72, 68.5, 67, 66.5, 66, 66, 64.5, 63, 63, 62.5, 61.5, 61, 60.5, 60.5, 60, 60, 59, 59, 59, 59, 59, 59, 58.5, 58, 58, 57, 56, 56, 55, 55, 54.5, 54.5, 53.5,
        53, 53, 52.5, 52, 51.5, 51, 50, 49.5, 48.5, 47.5, 46.5, 46.5, 46.5, 45.5, 45, 44.5, 44.5, 43.5, 43, 42.5, 42, 42, 42, 41, 40.5, 40, 40, 38, 38, 37.5, 35, 34.5, 33, 30.5, 28.5, 28.5, 27.5, 24.5, 22]
var = np.var(data)
std = np.std(data)
mean = np.mean(data)
median = np.median(data)
normal = np.random.normal(mean, std, 100000)
# PLOT APPROXIMATION OF NORMAL DISTRIBUTION AS DISTRIBUTION OF TEST GRADES
plt.hist(normal, bins=100)
plt.title("Normal distribution of test grades")
plt.xlabel("Test grades")
plt.ylabel("Frequency")
# LINE SHOWING MEAN
plt.axvline(mean, color='r', linestyle='solid', linewidth=2)
# LINE SHOWING MEDIAN
plt.axvline(median, color='b', linestyle='solid', linewidth=2)
# LINE SHOWING STANDARD DEVIATION
plt.axvline(mean + std, color='r', linestyle='dashed', linewidth=2)
plt.axvline(mean - std, color='r', linestyle='dashed', linewidth=2)
# LINE SHOWING ACTUAL GRADE OF 40.5
plt.axvline(40.5, color='g', linestyle='solid', linewidth=2)
plt.show()
#SCATTER PLOT OF TEST GRADES
count = np.arange(1, len(data) + 1)
plt.scatter(data, count) 
plt.xlabel("Test grades")
plt.ylabel("Count")
plt.title("Scatter plot of test grades")
plt.show()
