import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns
import folium


BFdata=pd.read_csv(r"accidents.csv")

#A
sns.catplot(x="Victims", hue="Part of the day", col="Month", data=BFdata, kind="count")
print('During Afternoon and Morning there are a lot of victims and don\'t change over time')

#B
sns.catplot(x="Vehicles involved",hue="Part of the day",col="Weekday",data=BFdata, kind="count")
print('During Monday, Tuesday, Thursday and Friday have the most car accidents. '
      'The mayority of the car accidents are in the morning and afternoon')

#C
sns.catplot(hue="Hour",x="Vehicles involved",col="Weekday",data=BFdata, kind="count")
print('From monday to friday the vehicles involved are incrementing by day between 7am to 7pm,'
      ' then drops on saturday and friday')

#D
sns.catplot(x="Victims",col="Weekday",data=BFdata, kind="count")
print('Friday')

#E
sns.catplot(x="Vehicles involved",col="Weekday",data=BFdata, kind="count")
print('Friday')

#F
group = BFdata.groupby("District Name").count()
plot = group.plot(kind='bar')
plot.get_legend().remove()

Barcelona_coordinates= (41.3887901, 2.1589899)

map=folium.Map(Barcelona_coordinates,zoom_start=12)

for each in BFdata[0:1000].iterrows():
    folium.Marker(location=[each[1]['Latitude'], each[1]['Longitude']], popup=str(each[1]['Victims'])).add_to(map)
map.save('Victims_Barcelona.html')
print('Eixample, Sant Marti, Sants-Montjuic, Sarria-Sant Gervasai')

#G
sns.catplot(col="District Name", x="Victims",data=BFdata, kind="count")
