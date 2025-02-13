# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:56:02 2025

@author: wenji
"""
import numpy as np
import pandas as pd
from datetime import datetime
import os
import matplotlib.pyplot as plt

#import 12 months of trip data
jan_tripdata = pd.read_csv("C:\\Users\\wenji\\OneDrive\\Desktop\\project\\excel file data\\202401-divvy-tripdata.csv",header = 0)
feb_tripdata = pd.read_csv("C:\\Users\\wenji\\OneDrive\\Desktop\\project\\excel file data\\202402-divvy-tripdata.csv",header = 0)
mar_tripdata = pd.read_csv("C:\\Users\\wenji\\OneDrive\\Desktop\\project\\excel file data\\202403-divvy-tripdata.csv",header = 0)
apr_tripdata = pd.read_csv("C:\\Users\\wenji\\OneDrive\\Desktop\\project\\excel file data\\202404-divvy-tripdata.csv",header = 0)
may_tripdata = pd.read_csv("C:\\Users\\wenji\\OneDrive\\Desktop\\project\\excel file data\\202405-divvy-tripdata.csv",header = 0)
jun_tripdata = pd.read_csv("C:\\Users\\wenji\\OneDrive\\Desktop\\project\\excel file data\\202406-divvy-tripdata.csv",header = 0)
jul_tripdata = pd.read_csv("C:\\Users\\wenji\\OneDrive\\Desktop\\project\\excel file data\\202407-divvy-tripdata.csv",header = 0)
aug_tripdata = pd.read_csv("C:\\Users\\wenji\\OneDrive\\Desktop\\project\\excel file data\\202408-divvy-tripdata.csv",header = 0)
sep_tripdata = pd.read_csv("C:\\Users\\wenji\\OneDrive\\Desktop\\project\\excel file data\\202409-divvy-tripdata.csv",header = 0)
oct_tripdata = pd.read_csv("C:\\Users\\wenji\\OneDrive\\Desktop\\project\\excel file data\\202410-divvy-tripdata.csv",header = 0)
nov_tripdata = pd.read_csv("C:\\Users\\wenji\\OneDrive\\Desktop\\project\\excel file data\\202411-divvy-tripdata.csv",header = 0)
dec_tripdata = pd.read_csv("C:\\Users\\wenji\\OneDrive\\Desktop\\project\\excel file data\\202412-divvy-tripdata.csv",header = 0)

dataframe = [jan_tripdata,feb_tripdata,mar_tripdata,apr_tripdata,may_tripdata,jun_tripdata,jul_tripdata,aug_tripdata,sep_tripdata,oct_tripdata,nov_tripdata,dec_tripdata]
column_name = jan_tripdata.columns.tolist()
month_list = []
for i in range(1,13):
    month_list.append(i)

"""
#1.	What is the trend of bicycle usage across 12 months?
number_of_rides = []
for data in dataframe:
    number_of_rides.append(data.shape[0])

plt.figure(figsize=(10,5))
plt.plot(month_list, number_of_rides, marker='o', linestyle='-', color='b', label="Total Rides")

# Add labels and title
plt.xlabel("Month")
plt.ylabel("Total Rides")
plt.title("Monthly Total Rides in 2024")
plt.legend()

# Improve visualization
plt.grid(True, linestyle="--", alpha=0.6)

# Show the plot
plt.show()
"""

"""
#2.People prefer classic bike or electric bike?
record_dict = {}

for month, data in zip(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], dataframe):
    # Count occurrences of 'electric_bike' and 'classic_bike' directly
    bike_counts = data["rideable_type"].value_counts()

    # Store the results in the dictionary
    record_dict[month] = {
        "electric": bike_counts.get("electric_bike", 0), 
        "classic": bike_counts.get("classic_bike", 0)
    }


bike_type = pd.DataFrame(record_dict).T
ax = bike_type.plot(kind="bar", figsize=(10, 6))
ax.set_xlabel('Month')
ax.set_ylabel('Bike Count')
ax.set_title('Monthly Bike Counts: Electric vs Classic')
ax.set_xticklabels(bike_type.index, rotation=45)
plt.show()
"""

"""
#3.	On average, how long does people ride?
average_ride_time = []

for data in dataframe:
    data["started_at"] = pd.to_datetime(data["started_at"])
    data["ended_at"] = pd.to_datetime(data["ended_at"])

    time_diff = (data["ended_at"] - data["started_at"]).dt.total_seconds()

    avg = time_diff.mean()
    
    average_ride_time.append(avg)

plt.figure(figsize=(10,5))
plt.bar(month_list, average_ride_time, color='b', label="Average Ride Time")

plt.xlabel("Month")
plt.ylabel("Average Ride Time")
plt.title("Monthly Average Ride Time in 2024")
plt.legend()
"""
"""
#4.What’s people behaviour using bikes on weekdays compare to weekends?
# Create lists to store results
weekday_avg_rides = []
weekend_avg_rides = []

for data in dataframe:  
   
    data["started_at"] = pd.to_datetime(data["started_at"])
    
    
    data["day_of_week"] = data["started_at"].dt.weekday  

    
    weekday_rides = data[data["day_of_week"] < 5].shape[0]
    weekend_rides = data[data["day_of_week"] >= 5].shape[0]

    weekday_avg_rides.append(weekday_rides / 5)  
    weekend_avg_rides.append(weekend_rides / 2) 

bar_width = 0.35  # Width of bars
x = range(len(month_list))  

plt.figure(figsize=(10, 5))
plt.bar(x, weekday_avg_rides, width=bar_width, label="Weekday Rides", color="b", alpha=0.7)
plt.bar([i + bar_width for i in x], weekend_avg_rides, width=bar_width, label="Weekend Rides", color="r", alpha=0.7)


plt.xlabel("Month")
plt.ylabel("Average Number of Rides")
plt.title("Average Rides on Weekdays vs. Weekends (2024)")
plt.xticks([i + bar_width / 2 for i in x], month_list)  # Set month labels at correct position
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the plot
plt.show()
"""
#5.What’s the difference between member and casual users in terms of riding time or frequency of usage
member_dict = {}

for month, data in zip(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], dataframe):
    # Count occurrences of 'electric_bike' and 'classic_bike' directly
    bike_counts = data["member_casual"].value_counts()

    
    member_dict[month] = {
        "member": bike_counts.get("member", 0), 
        "casual": bike_counts.get("casual", 0)
    }


bike_type = pd.DataFrame(member_dict).T
ax = bike_type.plot(kind="bar", figsize=(10, 6))
ax.set_xlabel('Month')
ax.set_ylabel('Ride Count')
ax.set_title('Monthly Bike Counts: Member vs Casual')
ax.set_xticklabels(bike_type.index, rotation=45)
plt.show()

