import matplotlib.pyplot as plt
import numpy as np

# Country names
countries = [
    "Norway", "Nepal", "Iceland", "China",
    "Viet Nam", "Singapore", "United Kingdom",
    "Switzerland", "European Union", "Uruguay",
    "Thailand", "Türkiye", "Israel", "Costa Rica",
    "Ukraine", "Indonesia", "UAE", "Australia",
    "New Zealand", "Jordan", "Korea", "Canada",
    "Colombia", "United States"
]

# Approximate values from the image
values1 = [
    75, 10, 52, 6, 0, 3, 11, 14, 10, 0,
    1, 0, 3, 2, 2, 0, 0, 1, 7, 2, 3, 4, 1, 2
]

values2 = [
    97, 68, 62, 53, 41, 40, 35, 34, 27, 28,
    23, 22, 21, 17, 16, 15, 10, 15, 12, 11,
    11, 11, 10, 10
]

# Colors
colors = [
    "deepskyblue", "orange", "deepskyblue", "coral",
    "orange", "orange", "deepskyblue", "deepskyblue",
    "royalblue", "mediumseagreen", "orange", "deepskyblue",
    "deepskyblue", "mediumseagreen", "deepskyblue", "orange",
    "yellow", "orange", "orange", "yellow",
    "orange", "deepskyblue", "mediumseagreen", "teal"
]

# Y positions
y = np.arange(len(countries))

# Create figure
plt.figure(figsize=(13, 8))

# Scatter plot
for i in range(len(countries)):
    plt.scatter(
        [values1[i], values2[i]],
        [y[i], y[i]],
        color=colors[i],
        s=110,
        edgecolors="gray",
        linewidths=1.5
    )

# Labels and formatting
plt.yticks(y, countries)
plt.xticks(np.arange(0, 101, 20))

plt.xlim(-2, 103)
plt.ylim(-0.6, len(countries)-0.4)

# Grid lines
plt.grid(axis="x", color="lightgray", linewidth=1, alpha=0.7)

plt.gca().invert_yaxis()

plt.title("Country-wise Electric Vehicle Comparison",
          fontsize=16, fontweight="bold")

plt.xlabel("Electric Vehicle Share (%)", fontsize=12)

plt.ylabel("Countries", fontsize=12)

plt.tight_layout()

plt.show()
