#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name:Ziyah // Fierce Bird ")
print("Clean the data and show which top 10 countries has the highest Undernourished rate as compared with their Population")
print("Show a comparison between Meat and Vegetables consumption across the countries")


# In[2]:


#predefine code for image
from IPython.display import Image
Image(filename='healthy.jpg') 
#predefine code end


# # Activity - 1 Clean the data and show which top 10 countries has the highest Undernourished rate as compared with their Population

# In[3]:


#import the required packages 
import pandas as pd
import matplotlib.pyplot as plt

#Read the csv file.
df = pd.read_csv("COVID-19 Healthy Diet Dataset.csv")
df


# In[4]:


#Cleaning data
df.replace( '<2.5',int(3),inplace=True)
df


# In[5]:


#Converting object datatype column to float datatype
df['Undernourished'] = df['Undernourished'].astype(float)
df['Undernourished'].dtypes


# In[6]:


#Groupby country and apply sum on Undernourished and Population column and create a new dataframe out of it
groupby_country=df.groupby('Country')['Undernourished',"Population"].sum().reset_index()
groupby_country


# In[7]:


#Sort the new dataframe as per Undernourished column
undernourished_sorted=groupby_country.sort_values(by=["Undernourished"],ascending = False)
undernourished_sorted


# In[8]:


#Get the top 10 countries from the sorted data
top_10=undernourished_sorted.head(10)
#Convert Undernourished percentage to number and add a new column to the top 10 countries dataframe
top_10['Percentage']=top_10['Undernourished']/100*top_10['Population']
top_10


# In[11]:


#Plot a stacked bar graph for showing the Population vs Undernourished rate
population=top_10['Population']
percent=top_10['Percentage']
country=top_10['Country']
plt.figure(figsize=(12,8))
plt.title('Undernourished rate as per Population')
plt.bar(country,population,bottom=percent,color="pink",label="country population")
plt.bar(country,percent,color="purple",label="Undernourished")
plt.legend()
plt.xticks(rotation=80)
plt.xlabel("Countries")
plt.ylabel("Population")
plt.show()


# Conclusion - 

# # Activity - 2 Show a comparison between Meat and Vegetables consumption across the countries

# In[12]:


#Sort the big dataframe as per Meat consumption
sorted_Meat = df.sort_values(by=['Meat'],ascending = False)
sorted_Meat


# In[13]:


#Sort the big dataframe as per Vegetables consumption
sorted_Veg = df.sort_values(by=['Vegetables'],ascending = False)
sorted_Veg


# In[17]:


#Plot a histogram showing the Meat consumption vs Vegetables consumption across countries 
plt.figure(figsize=(12,8))
Meat=sorted_Meat.head(20)
plt.hist(Meat, bins=20,label="Meat")
Veg=sorted_Veg.head(20)
plt.hist(Veg, bins=20,label="Vegatables")
plt.title('Meat Consumption vs Vegetables Consumption')
plt.xlabel('Food')
plt.ylabel('Consumption')
plt.show()


# Conclusion - 

# In[ ]:




