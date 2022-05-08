#!/usr/bin/env python
# coding: utf-8

# ## Importing modules

# In[363]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


# ## Reading data

# In[364]:


df = pd.read_csv("dataset.csv")


# In[365]:


df.info()


# In[366]:


df


# We can see from the data above that there are lot of missing values so we first replace '?' with null values and then use missing value imputation methods for easier code.

# ## Data cleaning

# In[367]:


# Replace '?' with null values
df.replace(to_replace = '?', value = np.NaN,inplace=True)


# In[368]:


df.columns


# In[369]:


# Remove all the null values in weather columns separately as the values should either be 0 or 1
weather_columns = [x for x in df.columns if 'wt' in x]
for i in weather_columns:
  df[i].fillna(0,inplace = True)


# In[370]:


df.info()


# In[371]:


#Convert the columns to float type
df[['wt_fog', 'wt_heavy_fog', 'wt_thunder', 'wt_sleet', 'wt_hail',
       'wt_glaze', 'wt_haze', 'wt_drift_snow', 'wt_high_wind', 'wt_mist',
       'wt_drizzle', 'wt_rain', 'wt_freeze_rain', 'wt_snow', 'wt_ground_fog',
       'wt_ice_fog', 'wt_freeze_drizzle', 'wt_unknown','casual','registered','total_cust','holiday']] = df[['wt_fog', 'wt_heavy_fog', 'wt_thunder', 'wt_sleet', 'wt_hail',
       'wt_glaze', 'wt_haze', 'wt_drift_snow', 'wt_high_wind', 'wt_mist',
       'wt_drizzle', 'wt_rain', 'wt_freeze_rain', 'wt_snow', 'wt_ground_fog',
       'wt_ice_fog', 'wt_freeze_drizzle', 'wt_unknown','casual','registered','total_cust','holiday']].apply(pd.to_numeric)


# In[372]:


df


# We can see all the null values in the weather columns has been cleaned. Now we will impute the missing values in temp_avg column. We take the average of temp_max and temp_min for now for simplicity.

# In[373]:


for i,value in enumerate(df['temp_avg']):
    if value in ['NaN','Na','NA',np.NaN]:
        df['temp_avg'][i] = (df['temp_max'][i] + df['temp_min'][i])/2
    else:
        df['temp_avg'][i] = df['temp_avg'][i]
df['temp_avg'] = df['temp_avg'].apply(pd.to_numeric)


# In[374]:


df.info()


# In[375]:


df.isnull().sum()


# Find out the missing values in the columns of total_customers

# In[376]:


df[df['casual'].isna()]


# We can see that the 4 missing values in the data is same for all the customers column. We can either impute the data or remove the rows. As it is a time series data, we do the forward filling imputation as the attributes are closer to each other generally in the next timestamp.

# In[377]:


df[['casual','registered','total_cust']] = df[['casual','registered','total_cust']].fillna(method = 'ffill')


# In[378]:


#Fill the values in holiday as 0 if it is not a holiday else it is given as 1
df['holiday'].fillna(0,inplace=True)


# In[379]:


#Round of the values to 2 decimal places
df_v2 = df.round(2)


# In[380]:


df_v2.isnull().sum()


# All the missing values in the data has been cleaned

# In[381]:


df_v2.info()


# In[382]:


#Cleaned data after missing values imputation
df_v2


# ## Creating new variables to simplify data analysis 

# As we have lots of weather variables, we will simplify the analysis by merging weather columns related to each other to decrease complexity into three categories: rain, fog and ice. All closely related attributes will go into the each if the created category

# In[383]:


df_v2['rain'] = df_v2['wt_freeze_rain'] + df_v2['wt_drizzle'] + df_v2['wt_hail'] + df_v2['wt_rain'] + df_v2['wt_thunder'] + df_v2['wt_unknown'] + df_v2['wt_freeze_drizzle']
df_v2['fog'] = df_v2['wt_fog'] + df_v2['wt_ground_fog'] + df_v2['wt_haze'] + df_v2['wt_heavy_fog'] + df_v2['wt_high_wind'] + df_v2['wt_ice_fog'] + df_v2['wt_mist']
df_v2['ice'] = df_v2['wt_drift_snow'] + df_v2['wt_glaze'] + df_v2['wt_sleet'] + df_v2['wt_snow'] 


# Make sure the values stay either 1 or 0. 

# In[384]:


df_v2['rain'] = df_v2['rain'].apply(lambda x: 0 if x==0 else 1)
df_v2['fog'] = df_v2['fog'].apply(lambda x: 0 if x==0 else 1)
df_v2['ice'] = df_v2['ice'].apply(lambda x: 0 if x==0 else 1)


# In[385]:


df_v2['rain'] = df_v2['rain'].astype('category')
df_v2['fog'] = df_v2['fog'].astype('category')
df_v2['ice'] = df_v2['ice'].astype('category')


# In[386]:


#Drop all the weather columns to simplify the dataframe
df_v2.drop(columns = weather_columns,inplace=True)


# We will use the date column to create more features such as year, month, day so analyse our data more

# In[387]:


df_v2['datetime'] = df_v2['date'].apply(pd.to_datetime)


# In[388]:


df_v2['year'] = pd.DatetimeIndex(df_v2['datetime']).year
df_v2['month'] = pd.DatetimeIndex(df_v2['datetime']).month_name()
df_v2['dayOfWeek'] = df_v2['datetime'].dt.day_name()


# In[389]:


df_v2


# In[ ]:





# In[ ]:





# ## Data analysis and visualisation 

# In this part we will see basic distribution of the data and plots regarding the same.

# In[390]:


#Plotting total customers during each year
sns.catplot(x='year',y='total_cust',kind='box',data=df_v2)


# We can infer from the above plot that the no of registered kept increasing overall during the years. The growth is fastest in the initial years and even though customers were increasing, the growth rate decreased during the recent years

# In[391]:


#Plotting total customers during each month
sns.catplot(x='month',y='total_cust',kind='box',data=df_v2)


# We can infer from the above plot that the number of customers were higher during the months of April to October typically during Summer and Fall where temperatures are at high compared to Spring and Winter where temperatures are too low so we can see that there are less number of customers overall during those seasons. We can also observe that there are few outliers we on a particular day in february for example, more number of people registered. We can assume there might be few special events that has caused more users to register on that particular day.

# In[392]:


#Plotting total customers per day of the week
sns.catplot(x='dayOfWeek',y='total_cust',kind='box',data=df_v2)


# From the above plot we can infer that the number of customers are slightly more during the weekdays compared to weekends. We can assume that many people travel to workplaces during weekdays and they use more rental bikes hence the higher number on weekdays

# In[393]:


#Plotting total customers during each weather conditions
plt.figure(figsize = [12, 10])
plt.subplot(2,2,1)
sns.boxplot(x='rain',y='total_cust',data=df_v2)
plt.subplot(2,2,2)
sns.boxplot(x='fog',y='total_cust',data=df_v2)
plt.subplot(2,2,3)
sns.boxplot(x='ice',y='total_cust',data=df_v2)


# From the plot above, we can analyse the customers behaviour during each particular weather conditions. Rain has only slight effect on the number of customers registered where as fog has a slightly more effect on the demand. But during the snow times, the demand for the rental bikes is very less as less cutomers chose to ride the bikes during snow.

# In[394]:


sns.boxplot(x='holiday',y='total_cust',data=df_v2)


# In the above plot we can see that, more number of customers booked bikes during non-holidays compared to holidays. We can deduce that going to work has an effect on the demand for the bikes from the above plot

# ## Correlation plots and analysis

# In[395]:


sns.pairplot(df_v2,vars = ['temp_avg','temp_min','temp_max','temp_observ','total_cust'])


# In the above plot, we are plotting scatter plots between the temperature values and total customers to observe the relation between them. We can see that there is a perfect linear relation between all temperature values. Also, the temperature features have a medium level linear relationship with the total customers registered

# In[396]:


sns.pairplot(df_v2,vars = ['wind','precip','total_cust'])


# We can infer from the above plot that wind and precipitation has almost no effect on the total customers 

# In[397]:


sns.heatmap(df_v2[['temp_min', 'temp_max', 'temp_observ', 'wind', 'precip', 'total_cust']].corr(),annot=True)


# The heatmap above provides more accurate relation among the variables. There is no significant correlation between wind, precip and the target variable but we can see that the temperature features has good amount with the target variable

# We will use the pearson coefficient test to see the linear relationship between temparature variable and the target variable to get more understanding

# In[398]:


print("Pearsonr test temp_avg ",pearsonr(df_v2['temp_avg'],df_v2['total_cust']))
print("Pearsonr test temp_max ",pearsonr(df_v2['temp_max'],df_v2['total_cust']))
print("Pearsonr test temp_min ",pearsonr(df_v2['temp_min'],df_v2['total_cust']))


# Pearson coefficient tells us how strong the relation is between two variables. From the above results we can see that temp_avg has stronger correlation with the target variable compared to temp_max and temp_min even though the difference is not much

# In[399]:


df_v2.describe()


# ## Time-series data specific analysis

# We are dealing with a time series data. Apart from looking at the correlation plots and disctribution plots, we have to see if the data is stationary or non stationary. We will first plot line plots over time to check if the data is stationary or not. 

# In[400]:


df_v2.plot(x='date',y='total_cust',title='Total customers registered over time')


# We can see from the above plot that our time series problem is non-stationary. We have to deal with this before modelling part. For now, we just analyse and make inferences visually and descriptively.

# In[ ]:





# In[ ]:





# In[ ]:




