---
Title: Rental Bike Demand Forecasting
Date: "April 2022"        
Author: Team 5, CMPE 255, San José State University


Header-includes: |
  \usepackage{booktabs}
  \usepackage{caption}
---

# Abstract

Bicycle-sharing programs have grown in quantity and popularity in cities all around the world during the last decade. Users can borrow bicycles for a fee on a very short-term basis through bicycle-sharing programs. The bicycle-sharing system has grown in popularity in numerous cities across the world in recent years. This allows users to borrow a bike from point A and return it to point B in Washington D.C, USA, however, they may just go on a ride and return it to the same area. Regardless, each bike may serve a number of people each day. It's a system that allows you to hire bicycles at an affordable price.

A user of the system may easily reach a dock inside the system to unlock or return bicycles, thanks to advances in information technology. These technologies also generate a plethora of data that may be utilized to investigate how people use these bike-sharing systems.


# Introduction

Time-series analysis and forecasting is one of the most popular data analysis method from long time ago. Time series forecasting in statistics is a method where we predict variables that change over time. We observe the historical data that changed over time and use that knowledge to observe the patterns and changes in the future. There are many use cases of time-series analysis and forecasting in many domains such as retail market, sales prection, stocks prediction and many more. In our problem, we have a time-series data related to bike rental service where customers rent a bike for the day and we need to forecast the demand i.e. the number of customers who will rent the bike depending on the conditions around him.

We have a dataset with data collected where each row is a day with variables such as temperature, weather conditions, wind, and the number of customers who rented the bike. Our task is to analyse the customer behaviour pattern in renting the bikes with regards to the various factors including temperature, time of the year, weather conditions and all other features we extract from the data. The dataset is a time-series data so we are trying to forecast the demand i.e. predict the number of customers over given future data based on past time data. 

# Methods
Our goal of the project is to forecast the number of customers expected to rent bikes given the previous data. Before jumping into data modelling, we have to process and clean the data to prepare the dataset for modelling. We will go through the data cleaning, data analysis and data processing in this section.

**1. Data Collection:** We have used dataset from openML. The link to the dataset is https://www.openml.org/search?type=data&status=active&id=43486&sort=runs, The dataset contains 2922 entries and 23 features. The entries are days from Jan 1st 2011 to Dec 31st 2018.

**2. Data Cleaning:** We have cleaned the data by removing null values from the data. As this is a time-series data, we cannot directly remove the entries even if the number of missing values is less as time series is a continuous data. So we have filled the missing values using meaningful methods such as forwadfill and values whereever it is appropriate. In the case of weather features, we replaced missing values with 0s as the data columns contains either 0 or 1 as its value by meaning. In case of customers, we used forward filling method as the data is time-series, so we assumed data would be closer to the entry of before date. In case of temp_avg, we calculated the average of max temperature and min temperature for now. (We are planning to fit a linear estimate with available data using temp_max, temp_min as features and temp_avg as target variable. Once we fit the model, we will fill the missing values using the trained model to get more accurate data)

**3. Create new features:** We have created new features by merging the weather attributes to simplify the data analysis and modelling. All the similar weather conditions have been categorised into three groups: ice, rain and fog. We also created year, month and day of the week from given datetime variable to gain insights from the data on customer behaviour.

**4. Data Analysis and Visualisation:**
We have plotted the following plots to infer few observations
- Box plot of total customers by each year<br/> <p align="center"> 
![box_plot_by_year](/paper/images/box_plot_by_year.jpg)<br/><br/> <p>
We can infer from the above plot that the no of registered users kept increasing overall during the years. The growth is fastest in the initial years and even though customers were increasing, the growth rate decreased during the recent years





- Box plot of total customers by month<br/> <p align="center"> 
![box_plot_by_month](/paper/images/box_plot_by_month.jpg)<br/><br/> <p>
We can infer from the above plot that the number of customers were higher during the months of April to October typically during Summer and Fall where temperatures are at high compared to Spring and Winter where temperatures are too low so we can see that there are less number of customers overall during those seasons. We can also observe that there are few outliers we on a particular day in february for example, more number of people registered. We can assume there might be few special events that has caused more users to register on that particular day.





- Box plot of total customers by day of the week<br/> <p align="center"> 
![box_plot_by_day](/paper/images/box_plot_by_day.jpg)<br/><br/> <p>
From the above plot we can infer that the number of customers are slightly more during the weekdays compared to weekends. We can assume that many people travel to workplaces during weekdays and they use more rental bikes hence the higher number on weekdays





- Box plot of total customers by weather<br/> <p align="center"> 
![box_plot_by_weather](/paper/images/box_plot_by_weather.jpg)<br/><br/> <p>
From the plot above, we can analyse the customers behaviour during each particular weather conditions. Rain has only slight effect on the number of customers registered where as fog has a slightly more effect on the demand. But during the snow times, the demand for the rental bikes is very less as less cutomers chose to ride the bikes during snow.





- Box plot of the total customers by holiday<br/> <p align="center"> 
![box_plot_by_holiday](/paper/images/box_plot_by_holiday.jpg)<br/><br/> <p>
In the above plot we can see that, more number of customers booked bikes during non-holidays compared to holidays. We can deduce that going to work has an effect on the demand for the bikes from the above plot





- Scatter plots of temperatures vs total customers<br/> <p align="center"> 
![pair_plot](/paper/images/pair_plot_df.jpg)<br/><br/> <p>
In the above plot, we are plotting scatter plots between the temperature values and total customers to observe the relation between them. We can see that there is a perfect linear relation between all temperature values. Also, the temperature features have a medium level linear relationship with the total customers registered





- Heatmap plot for correlation<br/> <p align="center"> 
![heatmap_df](/paper/images/heatmap_df.jpg)<br/><br/> <p>
The heatmap above provides more accurate relation among the variables. There is no significant correlation between wind, precip and the target variable but we can see that the temperature features has good amount with the target variable

**5. Time-series specific analysis:**
Since our data is time-series based, we will have time-series specific analysis plots.
- line plot of total customers over time<br/> <p align="center"> 
![time_plot](/paper/images/time_plot.jpg)<br/><br/> <p>
We can see from the above plot that our time series problem is non-stationary. We have to deal with this before modelling part. 
  
**What is Stationary?**
           When working with time-series data, 'stationarity' is one of the most important concepts that you'll encounter. Generally, stationary series are those whose properties don't change over time, such as the mean, variance, and covariance. The upward trend in the mean is clearly visible, since it varies (increases) with time. In other words, this is not a stationary series. A series is termed stationary if it does not exhibit a trend. 

**6. Further Analysis:** We plan to do further analysis to find out if our series is stationary or non-stationary using some popular statistical tests one of the test is ADF(Augmented Dickey Fuller) test. It can be used to determine whether a series is stationary and determine whether a unit root exists. As a result, it can also identify whether a series has diverged. If we are unable to reject the null hypothesis, we can say the series is non-stationary, and the other test we can use is Kwiatkowski–Phillips–Schmidt–Shin (KPSS) test,  we can get an idea if a time series is stationary around a mean or linear trend, or if it is non-stationary because of the unit root. A stationary time series has statistical characteristics that remain constant over time, such as the mean and variance. ADF test has hypothesis testing for difference stationary where as KPSS test looks for trend stationarity in the series. If our series has non-stationarity, we will convert our series to stationary using following methods:
- Differencing: Removes series dependencies on time. 
- Detrending: Removes trend effects from dataset
- Transformation: Converts into stationary using log transfer method

**7. Data Modelling:** After converting our time-series data to stationary, we will move to modelling the data. Our tentative plan for now is to perform a naive-univariate prediction only using the target variable. We will next use Random forest and then use ensemble methods at advanced level to analyse and compare the performance of different approaches. 
  
# Models

# Comparisons

# Example Analysis
  
# Conclusions
  
# References
