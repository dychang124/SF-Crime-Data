import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt

filepath = 'criminal.csv'
df = pd.read_csv(filepath)

def time_frequency(data) :
    column = 'Incident Time'
    time_periods = {"0:00-1:59": 0, "2:00-3:59": 0, "4:00-5:59": 0, "6:00-7:59": 0, "8:00-9:59": 0, "10:00-11:59": 0, "12:00-13:59": 0, "14:00-15:59": 0, "16:00-17:59": 0, "18:00-19:59": 0, "20:00-21:59": 0, "22:00-23:59": 0}

    for time in data[column]:
        if pd.isnull(time):  
            continue
        
        try:
            hour, minute = map(int, time.split(':'))
        except ValueError:
            raise ValueError(f"Invalid time format: {time}")

        # Match the time to a time period
        if 0 <= hour < 2:
            time_periods["0:00-1:59"] += 1
        elif 2 <= hour < 4:
            time_periods["2:00-3:59"] += 1
        elif 4 <= hour < 6:
            time_periods["4:00-5:59"] += 1
        elif 6 <= hour < 8:
            time_periods["6:00-7:59"] += 1
        elif 8 <= hour < 10:
            time_periods["8:00-9:59"] += 1
        elif 10 <= hour < 12:
            time_periods["10:00-11:59"] += 1
        elif 12 <= hour < 14:
            time_periods["12:00-13:59"] += 1
        elif 14 <= hour < 16:
            time_periods["14:00-15:59"] += 1
        elif 16 <= hour < 18:
            time_periods["16:00-17:59"] += 1
        elif 18 <= hour < 20:
            time_periods["18:00-19:59"] += 1
        elif 20 <= hour < 22:
            time_periods["20:00-21:59"] += 1
        elif 22 <= hour < 24:
            time_periods["22:00-23:59"] += 1
        else:
            raise ValueError(f"Time out of range: {time}")

    return time_periods

def day_of_week_frequency(data) :
    column = "Incident Day of Week"
    days = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}

    for day in data[column]:
        if pd.isnull(day):  
            continue
        
        if day in days:
            days[day] += 1
        else:
            print(f"Invalid day: {day}")  # Optional: print invalid day values

    return days

def police_district_frequency(data) :
    column = "Police District"
    districts = {'Central': 0, 'Tenderloin': 0, 'Ingleside': 0, 'Park': 0, 'Richmond': 0, 'Bayview': 0, 'Northern': 0, 'Southern': 0, 'Mission': 0, 'Taraval': 0}

    for district in data[column]:
        if pd.isnull(district):
            continue
        if district in districts:
            districts[district] += 1
    return districts

def larceny_subcategory_count(data):
    subcategory_counts = {}

    for _, row in data.iterrows():
        if not pd.isnull(row["Incident Category"]) and row["Incident Category"] == "Larceny Theft":
            subcategory = row["Incident Subcategory"]
            
            if pd.isnull(subcategory):
                subcategory = "Unknown"  

            if subcategory in subcategory_counts:
                subcategory_counts[subcategory] += 1
            else:
                subcategory_counts[subcategory] = 1

    return subcategory_counts

def plot_larceny_subcategories(subcategory_counts):
    labels = list(subcategory_counts.keys())
    values = list(subcategory_counts.values())

    # Calculate percentages for the legend
    total = sum(values)
    percentages = [f"{(value / total) * 100:.1f}%" for value in values]

    # Plot the pie chart
    plt.figure(figsize=(10, 8))
    wedges, _ = plt.pie(
        values,
        labels=None,  # No labels directly on the pie
        startangle=90,
        wedgeprops={'linewidth': 0.5, 'edgecolor': 'white'}  # Separate slices
    )
    plt.title("Distribution of Larceny Theft Subcategories", fontsize=14)
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular

    # Add a legend with labels and percentages
    plt.legend(
        loc="center left",
        bbox_to_anchor=(1, 0.5),
        labels=[f"{label}: {value} ({percentage})" for label, value, percentage in zip(labels, values, percentages)],
        fontsize=10
    )

    plt.tight_layout()
    plt.show()


time_frequencies = time_frequency(df)
print(time_frequencies)

day_frequencies = day_of_week_frequency(df)
print(day_frequencies)

district_frequencies = police_district_frequency(df)
print(district_frequencies)

subcategories = larceny_subcategory_count(df)
print(subcategories)

plot_larceny_subcategories(subcategories)