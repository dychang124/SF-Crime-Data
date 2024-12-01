# plot police_district_frequency(df) into a bar graph

import matplotlib.pyplot as plt
from crime_correlations import police_district_frequency

filepath = 'criminal.csv'
df = pd.read_csv(filepath)

police_frequencies = police_district_frequency(df)
districts = list(police_frequencies.keys())
incidents = list(police_frequencies.values())

plt.figure(figsize=(10, 6))
plt.bar(districts, incidents, width=0.5)

plt.xlabel('Police Districts', fontsize=15)
plt.ylabel('Number of Incidents', fontsize=15)
plt.title('Number of Incidents by Police District', fontsize=30)

plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout() # Adjust layout to prevent labels from overlapping

plt.show()


