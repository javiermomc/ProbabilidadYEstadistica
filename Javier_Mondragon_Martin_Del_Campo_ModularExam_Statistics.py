# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 13:09:04 2019

@author: Javier Mondragon
@id: A01365137
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import matplotlib.backends.backend_pdf
import seaborn as sns

real_estate_data = pd.read_csv("real_estate_db2.csv")

# Part I

# 1
print("1. ", "city is qualitative")

# 2
print("2. ", "rent_mean is continuous variable")

# 3
print("3. ", "area_code is an interval")

# 5
print("5. ", "is a statistic")

# 6
print("6. ", "yes")

# 7
print("7. ", "The value is an atypical, this means that this value affects "
             "the standar derivation and the mean making anomalies to those values, if the z value has that score in"
             "case of that score the value must be to the right of the graph in a bell shape and other type of graphs")

# Part II

# 8
std_male = np.std(real_estate_data['male_pop'])
std_female = np.std(real_estate_data['female_pop'])
print("8. ", "Coefficient of variation of male: ", std_male, "; female: ", std_female)

# 9
male_pop = real_estate_data['male_pop']

q_25_male = round(np.percentile(male_pop, 25), 2)
q_50_male = round(np.percentile(male_pop, 50), 2)
q_75_male = round(np.percentile(male_pop, 75), 2)

print("9. ", "Q_1: ", q_25_male, "\n   ", "Q_2: ", q_50_male, "\n   ", "Q_3: ", q_75_male, "\n")

# 10
print("10. ", "No, it will be above the 75%")

# 11
female_pop = real_estate_data['female_pop']

q_25_female = round(np.percentile(female_pop, 25), 2)
q_50_female = round(np.percentile(female_pop, 50), 2)
q_75_female = round(np.percentile(female_pop, 75), 2)

print("11. ", "Q_1: ", q_25_female, "\n   ", "Q_2: ", q_50_female, "\n   ", "Q_3: ", q_75_female, "\n")

# 12

def boxplot(data, q1, q2, q3, title, label):
    plt.boxplot(data, vert=False)
    p_25 = round(np.percentile(data, 25), 2)
    p_50 = round(np.percentile(data, 50), 2)
    p_75 = round(np.percentile(data, 75), 2)
    plt.text(p_25, 0.85, "$Q_{1}=$" + str(q1), fontsize=12)
    plt.text(p_50, 0.75, "$Q_{2}=$" + str(q2), fontsize=12)
    plt.text(p_75, 0.65, "$Q_{3}=$" + str(q3), fontsize=12)

    iqr = (q3) - (q1)

    lower = (q1) - (1.5 * (iqr))
    upper = (q3) + (1.5 * (iqr))

    plt.title(title)
    plt.xlabel(label)
    plt.show()

boxplot(male_pop, q_25_male, q_50_male, q_75_male, "Male population boxplot", "Population")
boxplot(female_pop, q_25_female, q_50_female, q_75_female, "Female population boxplot", "Population")

# 13

iqr_male = (q_75_male) - (q_25_male)

lower_male = (q_25_male) - (1.5 * (iqr_male))
upper_male = (q_75_male) + (1.5 * (iqr_male))

iqr_female = (q_75_female) - (q_25_female)

lower_female = (q_25_female) - (1.5 * (iqr_female))
upper_female = (q_75_female) + (1.5 * (iqr_female))

downliers=female_pop[female_pop<lower_female]
upperliers=female_pop[female_pop>upper_female]

outliers=[]
outliers.append(downliers)
outliers.append(upperliers)
print("13. ")
for each in outliers:
    print(" ", each)

# 14

# 15
print("15. ", "Yes, it would be an uncommon data")

# 16
print("16. ")
number_of_classes = int(round(math.log(male_pop.size) / math.log(2)))
plt.xlabel("Histogram of male population")
freq, bins, patches = plt.hist(male_pop, bins=number_of_classes, edgecolor="black")
plt.show()

number_of_classes = int(round(math.log(female_pop.size) / math.log(2)))
plt.xlabel("Histogram of female population")
freq, bins, patches = plt.hist(female_pop, bins=number_of_classes, edgecolor="black")
plt.show()

# 17
print("17. ", "Yes, it is skewed to the right, skewed to the right shape")

# 18
print("18. ", "Yes, it is skewed to the right, skewed to the right shape")

# 19
print("19. ", "Between 3728.26 and 5592.40")

# 20
print("20. ", "Between 3633.33 and 5450.0")