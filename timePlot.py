# plot bar graph by time_frequency(df)

import matplotlib.pyplot as plt
from crime_correlations import time_frequency

filepath = 'criminal.csv'
df = pd.read_csv(filepath)

time_frequencies = time_frequency(df)

time_periods = list(time_frequencies.keys())
frequencies = list(time_frequencies.values())

plt.figure(figsize=(16, 8))  # Adjust figure size for better visualization
plt.bar(time_periods, frequencies, width = 0.5)
plt.xlabel("Time Period", fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.title("Incident Time Frequency", fontsize=30)
plt.xticks(rotation=45, ha='right', fontsize=10) # Rotate x-axis labels for readability
plt.yticks(fontsize=10)

plt.tight_layout()  # Adjust layout to prevent labels from overlapping
plt.show()


