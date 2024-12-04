import matplotlib.pyplot as plt

# Populations of each police district
populations = {
    'Central': 69961, 
    'Southern': 65166, 
    'Bayview': 74191, 
    'Mission': 81913, 
    'Northern': 104067, 
    'Park': 63359, 
    'Richmond': 87890, 
    'Ingleside': 138002, 
    'Taraval': 155029, 
    'Tenderloin': 35902
}

# Number of crimes in each police district
crimes = {
    'Central': 33756, 
    'Tenderloin': 20779, 
    'Ingleside': 14718, 
    'Park': 9633, 
    'Richmond': 11610, 
    'Bayview': 17080, 
    'Northern': 27217, 
    'Southern': 26723, 
    'Mission': 28755, 
    'Taraval': 13991
}

# Calculate crime rates per 1,000 people for each district
crime_rates_per_1000 = {district: (crimes[district] / populations[district]) * 1000 for district in crimes}

# Sort districts by crime rate (highest to lowest)
sorted_crime_rates = sorted(crime_rates_per_1000.items(), key=lambda x: x[1], reverse=True)

# Extract district names and their crime rates
districts = [item[0] for item in sorted_crime_rates]
rates = [item[1] for item in sorted_crime_rates]

# Plot the histogram
plt.figure(figsize=(10, 6))
bars = plt.bar(districts, rates, width=0.5)

# Add crime rate labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.1f}', ha='center', va='bottom', fontsize=10)

plt.title('Crime Rate Per 1,000 People by Police District', fontsize=14)
plt.xlabel('Police District', fontsize=12)
plt.ylabel('Incidents per 1,000 People', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
