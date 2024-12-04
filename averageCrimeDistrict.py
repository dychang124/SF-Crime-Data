# average incidents a day for each Police District in descending order (without 'Out of SF' district)

import pandas as pd
import matplotlib.pyplot as plt

filepath = 'criminal.csv'
df = pd.read_csv(filepath)

# Calculate the average incidents per day for each police district
incidents_per_day = df.groupby('Police District')['Incident Date'].count()
average_incidents = incidents_per_day / len(pd.unique(df['Incident Date']))

# Exclude incidents that are 'Out of SF'
average_incidents = average_incidents.drop('Out of SF', errors='ignore')

# Sort in descending order
average_incidents_sorted = average_incidents.sort_values(ascending=False)


# Plotting
plt.figure(figsize=(10, 6))
plt.bar(average_incidents_sorted.index, average_incidents_sorted.values)
plt.xlabel('Police District', fontsize=12)
plt.ylabel('Average Incidents per Day', fontsize=12)
plt.title('Average Incidents per Day by Police District', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()

# Add labels to bars
for i, v in enumerate(average_incidents_sorted.values):
    plt.text(i, v, f'{v:.2f}', ha='center', va='bottom', fontsize=8)


plt.show()
