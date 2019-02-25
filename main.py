"""
Created on Tue Feb 19 13:39:47 2019

@author: VictorAVera
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import matplotlib.backends.backend_pdf
import seaborn as sns

pdf =matplotlib.backends.backend_pdf.PdfPages("Victor_Vera_Modularexam_Statistics.pdf")
estate=pd.read_csv("real_estate_db2.csv")

n=5
#city=estate["city"]
print("1.","It is quantitative")
print("2.","It is continous variable")
print("3.","It is nominal")
print("5","It is Statistic")
print("6","Yes, it is true ")
print("7\n","The Z score is defined as (X- (the mean))/ Standard deviation; when data it is nos bell shaped it means the information is all over the ranges and so it is not concentrated in some points ")

# parte 2
male=estate["male_pop"]
female=estate["female_pop"]


mmean = np.mean(male)
fmean = np.mean(female)

mstd = np.std(male)
fstd = np.std(female)

CVm= ((mmean/mstd)*100)
CVf= ((fmean/fstd)*100)

print("CVm.",CVm)
print("CVf.",CVf)

print ("\n8\n. CV of females has more variation")

Q_1m=np.percentile(male, 25)
Q_2m=np.percentile(male, 50)
Q_3m=np.percentile(male, 75)

print("\n9\n.")
print("Q1: ", Q_1m)
print("Q2: ", Q_2m)
print("Q3: ", Q_3m)

print("\n10.","Yes it would be in the lowest")

Q_1f=np.percentile(female, 25)
Q_2f=np.percentile(female, 50)
Q_3f=np.percentile(female, 75)

print("\n11.")
print("Q1: ", Q_1f)
print("Q2: ", Q_2f)
print("Q3: ", Q_3f)

print("\n12 & 13 \n.")
plt.boxplot(male,vert=False)
plt.title("kk")
plt.show()
plt.boxplot(female,vert=False)
plt.title("kfk")
plt.show()
IR = Q_3m-Q_1m
upperFence = Q_3m+1.5*IR
lowerFence = Q_1m-1.5*IR

upperoutliers = male [male>upperFence]
lowerdownliers = male [male<lowerFence]
print("upperoutliers\n", upperoutliers,"\n" ,"lowerdownliers\n",lowerdownliers,"\n")


print("\n15.","Yes it would")

print("\n16.")

number_of_classes = int(round(math.log(male.size) / math.log(2)))
freq, bins, patches = plt.hist(male, bins=number_of_classes, edgecolor="black")
plt.show()
number_of_classes = int(round(math.log(female.size) / math.log(2)))
freq, bins, patches = plt.hist(female, bins=number_of_classes, edgecolor="black")
plt.show()
# PROFESOR AQUI ESTAN LAS LINEAS DEL CODIGO PARA HACER LOS HISTOGRAMAS PERO SE ME JUNTABAN CON LA BOXPLOT Y SE ME MOVIAN DE LUGAR
#PERO ESAS SON LAS LINEAS

print("\n17.","Skewed to the right")
print("\n18.","Skewed to the right")
print("\n19.","2132")
print("\n20.","2198")