# plot day_of_week_frequency(df) into a bar graph

import matplotlib.pyplot as plt
from crime_correlations import day_of_week_frequency

filepath = 'criminal.csv'
df = pd.read_csv(filepath)

day_frequencies = day_of_week_frequency(df)
days = list(day_frequencies.keys())
incidents = list(day_frequencies.values())

plt.figure(figsize=(10, 6))
plt.bar(days, incidents, width=0.5)

plt.xlabel('Day of the Week', fontsize=15)
plt.ylabel('Number of Incidents', fontsize=15)
plt.title('Number of Incidents by Day of the Week', fontsize=30)

plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout() # Adjust layout to prevent labels from overlapping

plt.show()


