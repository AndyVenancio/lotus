import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Given attributes
minimum = 17.5
maximum = 41.0
mean = 36.47
median = 37.0
std_dev = 3.86

# Generate data points for the normal distribution
x = np.linspace(minimum, maximum, 1000)
y = norm.pdf(x, mean, std_dev)

# Plot the normal distribution
plt.plot(x, y, label='Normal Distribution')

# Highlight the mean and median on the plot
plt.axvline(mean, color='r', linestyle='--', label='Mean')
plt.axvline(median, color='g', linestyle='--', label='Median')
plt.axvline(40, color='purple', linestyle='--', label='Score of 40')

# Add labels and legend
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Normal Distribution')
plt.legend()

# Show the plot
plt.show()
