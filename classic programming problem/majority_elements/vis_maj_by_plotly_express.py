from collections import Counter
import matplotlib.pyplot as plt
from majority_elements import results as data


maj = [data[n]['maj'] for n in range(len(data))]

# Extract values for 'avg', 'min', 'mid', and 'max'
avg_values = [entry['avg'] for entry in maj]
min_values = [entry['min'] for entry in maj]
mid_values = [entry['mid'] for entry in maj]
max_values = [entry['max'] for entry in maj]

# Count the occurrences for each attribute
avg_counts = Counter(avg_values)
min_counts = Counter(min_values)
mid_counts = Counter(mid_values)
max_counts = Counter(max_values)

# Plot pie charts for each attribute
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 'avg'
axes[0, 0].pie(avg_counts.values(), labels=avg_counts.keys(), autopct='%1.1f%%', startangle=140)
axes[0, 0].set_title('Majority Elements Pie Chart (avg)')

# 'min'
axes[0, 1].pie(min_counts.values(), labels=min_counts.keys(), autopct='%1.1f%%', startangle=140)
axes[0, 1].set_title('Majority Elements Pie Chart (min)')

# 'mid'
axes[1, 0].pie(mid_counts.values(), labels=mid_counts.keys(), autopct='%1.1f%%', startangle=140)
axes[1, 0].set_title('Majority Elements Pie Chart (mid)')

# 'max'
axes[1, 1].pie(max_counts.values(), labels=max_counts.keys(), autopct='%1.1f%%', startangle=140)
axes[1, 1].set_title('Majority Elements Pie Chart (max)')

plt.tight_layout()
plt.show()