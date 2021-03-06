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

**Time Series:**
    A stationary time series is a series whose properties such as mean, variance and autocorrelation doesn’t change over time. If the properties change over time, then it is non-stationary series. We should ensure that the series is stationary in order to forecast correctly and if the series is non-stationary, we convert it to stationary. Stationarity is preferred because if the mean and variance increase over time, it is difficult to forecast as the series is changing over time.
Augmented Dickey Fuller (ADF) test and Kwiatkowski–Phillips–Schmidt–Shin (KPSS) test are used to evaluate if a series is stationary or non-stationary.
 
**What is Stationary?**
           When working with time-series data, 'stationarity' is one of the most important concepts that you'll encounter. Generally, stationary series are those whose properties don't change over time, such as the mean, variance, and covariance. The upward trend in the mean is clearly visible, since it varies (increases) with time. In other words, this is not a stationary series. A series is termed stationary if it does not exhibit a trend. 

**6. Further Analysis:** We plan to do further analysis to find out if our series is stationary or non-stationary using some popular statistical tests one of the test is ADF(Augmented Dickey Fuller) test. It can be used to determine whether a series is stationary and determine whether a unit root exists. As a result, it can also identify whether a series has diverged. If we are unable to reject the null hypothesis, we can say the series is non-stationary, and the other test we can use is Kwiatkowski–Phillips–Schmidt–Shin (KPSS) test,  we can get an idea if a time series is stationary around a mean or linear trend, or if it is non-stationary because of the unit root. A stationary time series has statistical characteristics that remain constant over time, such as the mean and variance. ADF test has hypothesis testing for difference stationary where as KPSS test looks for trend stationarity in the series. If our series has non-stationarity, we will convert our series to stationary using following methods:
- Differencing: Removes series dependencies on time. 
- Detrending: Removes trend effects from dataset
- Transformation: Converts into stationary using log transfer method

**7. Data Modelling:** After converting our time-series data to stationary, we will move to modelling the data. Our tentative plan for now is to perform a naive-univariate prediction only using the target variable. We will next use Random forest and then use ensemble methods at advanced level to analyse and compare the performance of different approaches. 
  
# Models

Ensemble means combining multiple models to make predictions instead of one model.Ensemble learning offers a out of the box approach to combine the predictive power of multiple learning models. The models that participates in forming the ensemble is called base learners. Ensemble uses two types of methods:

**1. Bagging–**  It means that to create different set of training subsets with replacement and output is decided based on the majority voting. For instance Random Forest

**2. Boosting–** It uses sequential models with the combination of weak learners and strong learners that result into high accuracy.For instance XG BOOST, ADA BOOST, Gradient BOOST. Here, the focus is to built trees sequentially in such a way that each subsequent trees is aimed at reducing the errors of the previous tree model.

**Bagging meta-estimator** 
 It is an ensembling method which includes steps like creating random subsets from dataset which includes all features, than a base estimator is set on each of these sets and at the end all the predicted results from each of the subset model is combined to get result.The hyper parameters used are 

 - base_estimator: It indicates the base estimator  to fit a random subsets of a dataset
 - n_estimators: Number of base estimator which is required
 - n_jobs: number of jobs to be run in parallel
 - random_state:It is used to specify the method of random split. This parameter is used when comparison between 2 models is to be needed.

**Adaptive Boost** 

  AdaBoost is a decision tree with one level which is a decision tree with just one split. It builds a model and gives equal weights to all the data points and then assigns higher weights to points which shows highest errors. Now all the points which have higher weights are given more importance in the next model. It will keep training models until and unless a low error is received for the regression problem. When there is some non-linearity in our dataset this algorithm helps as it captures these non-linearities which in end contributes to better accuracy on the regression problem.


**Gradient Boosting**

As stated above sequential models are built here and they try to reduce the errors of previous models. The speciality is that errors are reduced by building a new model based on the errors of the previous model. It minimizes loss function by adding week learners with help of gradient descent.

The hyper parameters chosen are n_estimators,Learning rate,max_depth etc.  N_estimators is the number of trees (weak learners) that should be there in the model. For the learning rate the low value always works better provided that there are sufficient number of trees present. Max_depth is the related to the height of the decision. There are various extension of Gradient boosting which can be explored.


**XGBoost**

XGboost stands for eXtreme Gradient Boosting.It is one of the methods under boosting. It outperforms other models due to following features:
XGboost penalizes models through L2 and L1 regularization which is used to prevent overfitting. Our data contains one hot encoded values which shows that data is sparse. So there is a need of sparsity aware split finding algorithm for handling different types of sparsity patterns in data. In terms of computation also XGboost outperforms as it uses multiple cores on CPU. It is used when there is large number of training samples. Also when there is a mix numerical and categorical data XGboost is preferred.


**CatBoost**

To handle categorical variables is a tiresome operation, especially when there is a large number of such variables. When your categorical variables have too many labels, performing one-hot-encoding such data exponentially increases the dimension of the model and it becomes really tedious of preprocessing and training the dataset while avoiding overfitting.

The benefit that CatBoost provides is that it can automatically deal with categorical variables and does not require extensive data preprocessing before giving the data to the machine learning model.



# Comparisons
  
The main step in any machine learning model is the evaluation of model accuracy. The Mean absolute error, Mean Squared Error, R-Squared or Coefficient of determination and Root Mean Squared Error metrics are used to evaluate the performance/accuracy of the model in regression analysis problems.

**MAE:** The Mean absolute error is the  average of the absolute difference between the predicted values and the actual values.

**MSE:** It represents the average of the squared difference between the actual and predicted values. It measures the variance of the errors.

**RMSE:** The square root of Mean Squared error is Root Mean Squared Error.

**R-squared or coefficient of determination:** It is the proportion of the variance in the dependent variable. It is a scale-free score i.e. the value of R square will be less than one only even if of the values being small or large.

How to choose between them for the determination of the accuracy of the model?

Mean Squared Error(MSE) and Root Mean Square Error penalizes the large prediction errors with regard to Mean Absolute Error (MAE). But RMSE is generally preferred than MSE for the evaluation of the performance of the regression problems compared to other models. The lower value of MAE, MSE, and RMSE indicates higher accuracy of a regression model. MSE is a easy in terms of computation time unlike MAE. It is because former is differentiable while the later is non-differentiable. Thus, mostly RMSE is used as metric for calculating accuracy in terms of some loss function. For the comparison of accuracy of different models, RMSE is preferred than R-Squared
To conclude both RMSE and R-Squared tells how well a regression model is best suited for a particular dataset . To be specific RMSE tells how a regression model is used to predict the value of a response variable while on the other hand R-Squared tells how  well the predicted variables is able to tell about the variation in the response variable type.

Also random_state hyperparameter of model discussed is used for comparison between different models

<br/> <p align="center"> 
![Comparison](/paper/images/Comparison.png)<br/><br/> <p>

  
# Conclusions
To conclude,in this project, we tried to explore various regression techniques on a bike sharing dataset. We compared the performance of these regressors by using many metrics used for determination of the accuracy. AdaBoost regressor significantly outperformed other regressors in accuracy in terms of all the metrics used for comparison but we will choose XG boost so as to avoid overfitting.
  
We can improve the predictions accuracy by including more features in the dataset in future by making the model robust. Model strength can be increased by implementing advanced Machine Learning models.
  
# References
  
  1. https://scikit-learn.org/stable/modules/ensemble.html
  2. https://www.analyticsvidhya.com/blog/2021/10/a-comprehensive-guide-to-time-series-analysis/
  3. https://medium.com/analytics-vidhya/mae-mse-rmse-coefficient-of-determination-adjusted-r-squared-which-metric-is-better-cd0326a5697e
