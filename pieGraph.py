# graph pie chart to show the number of each 'Incident Category' and combine those has less than 2.5% + 'Other miscellaneous' as 'Other'

import pandas as pd
import matplotlib.pyplot as plt

filepath = 'criminal.csv'
df = pd.read_csv(filepath)

incident_counts = df['Incident Category'].value_counts(normalize=True) * 100

# Combine categories less than 2.5% into 'Other'
threshold = 2.5
other_categories = incident_counts[incident_counts < threshold].index
df['Incident Category'] = df['Incident Category'].replace(other_categories, 'Other')

# Combine 'Other' with 'Other Miscellaneous'
df['Incident Category'] = df['Incident Category'].replace('Other Miscellaneous', 'Other')

incident_counts = df['Incident Category'].value_counts()

# Pie chart
plt.figure(figsize=(10, 10))
color = ['#fe4848', 'orange', 'yellow', '#50ff92', '#7aec0f', '#18ecdf', '#18b6ec', '#b11ef6', '#fe48a9', '#4043e7', '#ccad6c' , '#a395ca', '#849da4']
plt.pie(incident_counts, labels=[f'{category} ({count})' for category, count in incident_counts.items()], autopct='%1.1f%%', startangle=90, colors = color)
plt.title('Incident Category Distribution', fontsize=20)

plt.show()
