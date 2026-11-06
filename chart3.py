import matplotlib.pyplot as plt
import numpy as np

# Years
years = ['2018', '2019', '2020', '2021',
         '2022', '2023', '2024']

x = np.arange(len(years))
width = 0.6

# Charging points by speed (Millions)
slow = [0.35, 0.60, 0.90, 1.20, 1.85, 2.65, 3.40]
fast = [0.18, 0.25, 0.38, 0.55, 0.85, 1.35, 1.85]
ultra = [0.02, 0.03, 0.02, 0.05, 0.10, 0.12, 0.15]

# Charging points by region (Millions)
china = [0.25, 0.50, 0.80, 1.15, 1.80, 2.75, 3.60]
europe = [0.15, 0.18, 0.25, 0.35, 0.55, 0.75, 1.05]
usa = [0.08, 0.10, 0.12, 0.15, 0.10, 0.15, 0.20]
rest = [0.08, 0.12, 0.13, 0.15, 0.35, 0.45, 0.55]

# Create two subplots
fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(16, 8)
)

# LEFT CHART - By speed
ax1.bar(x, slow, width, label='Slow',
        color='#42c5e5', edgecolor='black')

ax1.bar(x, fast, width, bottom=slow,
        label='Fast', color='#55e88b',
        edgecolor='black')

bottom = np.array(slow) + np.array(fast)

ax1.bar(x, ultra, width, bottom=bottom,
        label='Ultra-fast', color='#a66bd4',
        edgecolor='black')

ax1.set_title('By speed', fontsize=16, fontweight='bold')
ax1.set_ylabel('Million', fontsize=13)
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.set_ylim(0, 6)
ax1.grid(axis='y', alpha=0.3)
ax1.set_axisbelow(True)
ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.09),
           ncol=3, frameon=False)

# RIGHT CHART - By region
ax2.bar(x, china, width, label='China',
        color='#e84a50', edgecolor='black')

ax2.bar(x, europe, width, bottom=china,
        label='Europe', color='#3978c5',
        edgecolor='black')

bottom = np.array(china) + np.array(europe)

ax2.bar(x, usa, width, bottom=bottom,
        label='United States', color='#17b5a5',
        edgecolor='black')

bottom = bottom + np.array(usa)

ax2.bar(x, rest, width, bottom=bottom,
        label='Rest of World', color='#bdbdbd',
        edgecolor='black')

ax2.set_title('By region', fontsize=16, fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(years)
ax2.set_ylim(0, 6)
ax2.grid(axis='y', alpha=0.3)
ax2.set_axisbelow(True)
ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.09),
           ncol=4, frameon=False)

# Main title
fig.suptitle(
    'Global stock of public charging points by speed and region, 2018-2024',
    fontsize=17, fontweight='bold', color='#24476b'
)

plt.tight_layout(rect=[0, 0.08, 1, 0.93])
plt.show()
