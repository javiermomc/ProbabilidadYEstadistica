import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns
import folium

BFdata = pd.read_csv(r"accidents.csv")
sns.catplot(x="Victims", hue="Part of the day", col="Month", data=BFdata, kind="count")
plt.show()

avocado = pd.read_csv(r"accidents.csv")
sns.relplot(x="Victims", y="Part of the day", col="Month", hue="Serious injuries", data=avocado)
plt.show()

BFdata = pd.read_csv(r"accidents.csv")
sns.catplot(x="Vehicles involved", hue="Day", col="Part of the day", data=BFdata, kind="count")
plt.show()

BFdata = pd.read_csv(r"accidents.csv")
sns.catplot(y="Day", hue="Hour", col="Part of the day", data=BFdata, kind="count")
plt.show()

# San_Francisco_coordinates = (37.76, -122.45)
# crime_data = pd.read_csv("Police_Department_Incident_Reports__2018_to_Present.csv")
# map = folium.Map(San_Francisco_coordinates, zoom_start=12)
#
# for each in crime_data[0:100].iterrows():
#     folium.Marker(location=[each[1]['Latitude'], each[1]['Longitude']], popup=each[1]['Incident Description']).add_to(map)
# map.save('SanFranciscoCrimes.html')
# print('Saved!')
