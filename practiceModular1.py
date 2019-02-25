import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import matplotlib.backends.backend_pdf
import seaborn as sns
# We create the pdf object, where
# the plots of interest will be drawn
pdf =matplotlib.backends.backend_pdf.PdfPages(
"Output.pdf")
#We read the data and we store it in the PARKING DATA variabLE
parking_data=pd.read_csv("parking_citations.csv")
# Storing the information of Average Price column
# of the excel file to a variable called average_price
time_issue=parking_data["Issue time"]
# If you get just the data from the excel
# sometimes it happens that nasty values are stored
# So they are considered as rubish data by Python
# It will consider them as NaN (Non a Value)
# In such cases, the following line of code makes the magic of cleaning
# the data that contains nan values.
# The nan values can make our functions break. For example the percentile
# function and the boxplot will not work properly.
# So in the following line of code we clean firstly the data of all possible
# NaN Values.
filtered_data=time_issue[~np.isnan(time_issue)]
# We create a figure to plot
figure=plt.figure(figsize=(8,30))
n=5
mean=np.mean(filtered_data)
# We calculate the standard deviation
# The variable ddof is telling to calculate as a sample
# Instead of a population
std=np.std(filtered_data,ddof=1)
ax=figure.add_subplot(n,1,1)
# We calculate the number of classes with our rule of
# n=log(sizeofdata)/log(2)
# We use the int and round so that we have an integer number
number_of_classes=int(round(math.log(filtered_data.size)/math.log(2)))
#Our first plot
freq,bins,patches=plt.hist(filtered_data,
edgecolor="Black",bins=number_of_classes)
class_range=[]
# We will create an array of upper_classes.
#We make it firstly emoty so that we can actually append new values.
upper_class=[]
# We will create an array of middle_classes.
#We make it firstly emoty so that we can actually append new values.
# This array will contain the mark of classes that
# is just the average of the upper and lower class
middle_class=[]
# We loop over all the elements of the bins array
#which contains the classes limits
# We append the corresponding values.
for i in range(int(bins.size)-1):
    lower=bins[i]
    upper=bins[i+1]
    upper_class.append(upper)
    middle_class.append((upper+lower)/2)
    class_range.append("{:0.2f}".format(lower)+"-"+"{:0.2f}".format(upper))

rel_freq=freq/filtered_data.size

plt.title("Histogram of Time Parking Issue in Los Angeles")
plt.xlabel("Time in Seconds")
plt.ylabel("Number of Issues")
print("No, it is not bell shaped visually. It is skewed to the left")
print("Number of classes=",number_of_classes)
print("The 68% of the data lies in the range (",mean-std,mean+std,") according to the Empirical Rule")
print("The 95% of the data lies in the range (",
mean-2*std,mean+2*std,
") according to the Empirical Rule")
print("The 99.7% of the data lies in the range (",
mean-3*std,mean+3*std,
") according to the Empirical Rule")
#---------------------------
ax=figure.add_subplot(n,1,2)
#When we tell to plt.hist() function to be cumulaive as true, then
# the plot will be cumulative histogram
cum_freq,trash1,trash2=plt.hist(filtered_data,edgecolor="Black",
bins=number_of_classes,cumulative=True)
plt.title("Cumulative Histogram of Time a Parking Issue took in Los Angeles")
plt.xlabel(" Time in Seconds")
plt.ylabel("Cumulative Frequency of Time Issue")
ax=figure.add_subplot(n,1,3)
ax.plot(upper_class,cum_freq,'ro-')
plt.title("Ogive of Time a Parking Issue took in Los Angeles")
plt.ylabel("Cumulative Frequency of Time a Parking Issue took in Los Angeles")
plt.xlabel("Time in seconds")
ax=figure.add_subplot(n,1,4)
plt.boxplot(filtered_data,vert=False)
plt.xlabel("Time in seconds")
Q_1=np.nanpercentile(filtered_data,25)
Q_2=np.nanpercentile(filtered_data,50)
Q_3=np.nanpercentile(filtered_data,75)
IQR=Q_3-Q_1
upper_fence=Q_3+1.5*IQR
lower_fence=Q_1-1.5*IQR
downliers=filtered_data[filtered_data<lower_fence]
upperliers=filtered_data[filtered_data>upper_fence]
outliers=[]
outliers.append(downliers)
outliers.append(upperliers)
noutliers=np.array(outliers)
z_values=(noutliers-mean)/std
print("Q_1=",Q_1)
print("Q_2=",Q_2)
print("Q_3=",Q_3)
print("The lower fence is ",lower_fence)
print("The upper fence is ",upper_fence)
values_to_check=np.array([1500,1.45,205,1655,311,390,4,23,256,248])
# For this part you could have calculated by hand
# and then making your program to print the answer
# What is done is the following
# with the for loop we go all over from 0,1,2...., up to the size
# of the array of values_to check. The we compare
#if they are lower than the lower fence or greater than the upper fence
for i in range(values_to_check.size):
    if values_to_check[i]<lower_fence or values_to_check[i]>upper_fence:
        print("The value ", values_to_check[i],
            " seconds would be an uncommon time of parking issue")
    else:
        print("The value ", values_to_check[i],
            "secons would be a common time of parking issue")
Table=pd.DataFrame({"Time of Parking Issue":freq,
"Relative Frequency":rel_freq,
"Mark of Class":middle_class})
Table.to_excel("ExcelOutput.xlsx",
float_format="%.2f")
print("The outliers are",outliers )
print("The z values are",z_values)
ax=figure.add_subplot(n,1,5)
plt.title("Polygon of Frequencies of the Time Parking Issue in Los Angeles")
plt.ylabel("Number of Issues ")
plt.xlabel("Time in seconds")
R_class=bins[1]-bins[0]
mcfp=middle_class
print(middle_class[-1])
print(R_class)
mcfp.insert(int(len(middle_class)),middle_class[-1]+R_class)
mcfp.insert(0,middle_class[0]-R_class)
#frequencies for polygon
ffp=freq.tolist()
ffp.append(0)
ffp.insert(0,0)
ax.plot(mcfp,ffp,"-ro")
pdf.savefig(figure)
figure2=plt.figure(figsize=(15,15))
cmap=plt.get_cmap('RdYlBu')
acolors=[cmap(i) for i in np.linspace(0,1,8)]
cars=parking_data["Make"].value_counts()
4
cars_final=cars[cars>=5000]
# The second set, only those values below 2000 and greater than 150 (the second cut in following lines), The rest is contained as Very Unlikely Jobs
less_common_cars=cars[cars<5000]
less_common_cars=less_common_cars[less_common_cars>100]
extremely_unlikely=less_common_cars[less_common_cars<100]
# # We need to include the less common jobs to all jobs so we create another pandas object
other=pd.Series([less_common_cars.sum()],index=["Less Common Cars"])
Extremely_unlikely=pd.Series([extremely_unlikely.sum()],index=["Extremely Unlikely"])
cars_final=cars_final.append(other)
less_common_cars=less_common_cars.append(Extremely_unlikely)
# The explode array will be used to offset categories
# of the pie chart. So the way it works is the following
# The function plt.pie() recieves an array , where each
# value is how much you want to offset certain categorie
# So for example, suppouse you have in regions the following
# San Francisco 10
# New York 20
# Houston 20
# Dallas 30
# Now, if you tell explode=[0,0,0,1]
# Then the dallas piece of the chart will be offset by 1 fraction of the
#radius with which to offset each wedge
# Suppouse you said explode=[0,1,0,0]
# Then the New York would be offset
# So, what we do with the following code is to offset certain
# values of the chart.
# Firstly we create an array of zeros of the size of regions
# with np.zeros(regions.size). Numpy has the ability to
# create an array of the size of our interest with just that
# line of code.
# After that we offset just the last three elements
# we substitute the zero values that the last (-1)
# the penultimate (-2) and the antepenultimate(-3)
# had and we say the exact value we want to offset
# Therefore when we call the function
# plt.pie() just three elements will be offset, because
#all the others where offset just zero , i.e. , they didnt move at all!
explode1=np.zeros(cars_final.size)
for i in range(22):
    explode1[-i]=1.5-0.02*i
alabels=[cars_final.index[i] +" "+
    "{:0.3f}".format(cars_final[i]/parking_data["Issue time"].size*100)+
    "%" for i in range (cars_final.size)]
ax=figure2.add_subplot(2,1,1)
plt.pie(cars_final,explode=explode1,labels=alabels)
print("The car with more parking issues in LA is Toyota")
print("The time for solving a parking issue is ", mean)
median=np.median(filtered_data)
print("The median time for solving a parking issue is ",median)
print("The standard deviation for solving a parking issue is",std)
lscmmnlabels=[less_common_cars.index[i] +" "+
"{:0.3f}".format(less_common_cars[i]/parking_data["Issue time"].size*100)+
"%" for i in range (less_common_cars.size)]
ax=figure2.add_subplot(2,1,2)
explode2=np.zeros(less_common_cars.size)
for i in range(less_common_cars.size):
    explode2[-i]=1.5-0.02*i
plt.pie(less_common_cars,labels=lscmmnlabels,explode=explode2)
matplotlib.pyplot.subplots_adjust(hspace=0.8)
sns.catplot(y="Color",data=parking_data,kind="count",height=10)
pdf.close()
