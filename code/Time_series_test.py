#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[51]:


import pandas as pd
import numpy as np
import math
import pickle
from scipy.stats import kruskal, pearsonr, randint, uniform, chi2_contingency, boxcox
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, FunctionTransformer, StandardScaler, power_transform
from sklearn.linear_model import SGDClassifier
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_squared_log_error, mean_absolute_error
from sklearn.model_selection import cross_val_score, cross_validate, TimeSeriesSplit, RandomizedSearchCV, GridSearchCV, cross_val_predict
from datetime import datetime
from statsmodels.tsa.stattools import grangercausalitytests, adfuller, kpss, acf, pacf
from collections import defaultdict, OrderedDict
from sklearn.base import BaseEstimator, TransformerMixin, RegressorMixin
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from sklearn.decomposition import PCA
from statsmodels.tsa.ar_model import AR
from sklearn.linear_model import LinearRegression
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import mean_absolute_error
import seaborn as sb
import matplotlib.pyplot as plt 

get_ipython().run_line_magic('matplotlib', 'inline')


# In[52]:


df_v2 = pd.read_csv("df_v2.csv")


# In[53]:


df_v2


# In[54]:


df_v2.describe()


# In[55]:


df_v2.columns


# In[56]:


df_v2['total_cust']


# In[57]:


#In this step, we compute the difference of consecutive terms in the series. 
#Differencing is typically performed to get rid of the varying mean.
#We will also perform log transform
df_v2['total_cust_log'] = np.log(df_v2['total_cust'])
df_v2['total_cust_diff'] = df_v2['total_cust_log']-df_v2['total_cust_log'].shift(periods=1, freq=None, axis=0, fill_value=0)
df_v2['total_cust_diff'].dropna().plot()


# When learning about time series, we came to know that to make to make time series stationary there are certain tests which needs to be done. These test are as per mentioned in the online resources available used for handling stationary time series.

# In[59]:


#Augmented Dickey Fuller Test to make the time series stationary
def adf_test(df, col_names):
    for name in col_names:
        print ('Results of Augmented Dickey-Fuller Test for {}'.format(name))
        result_test = adfuller(df[name], autolag='AIC')
        result_output = pd.Series(result_test[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
        for key, val in result_test[4].items():
            result_output['Critical Value (%s)'%key] = val
        print (result_output)


# In[60]:


testing_df = pd.DataFrame()
testing_features = [ 'precip','fog','temp_min', 'temp_max','wind','total_cust']

for col in testing_features:
    col_mean = df_v2[col].rolling(16).mean()[15:-1]
    col_std = df_v2[col].rolling(16).std()[15:-1]
    testing_df[col+'_mean16'] = col_mean.values
    testing_df[col+'_std16'] = col_std.values


# In[61]:


## adf test for total_customers
from statsmodels.tsa.stattools import adfuller
adf_test(df_v2, ['total_cust'])


# In[63]:


# adf test for total_cust_total-2
adf_test(df_v2, ['total_cust_diff'])


# In[64]:


adf_test(testing_df, testing_df.columns)


# ADF (Augmented Dickey Fuller) Test:
# The Dickey Fuller test is one of the statistical tests. It can be used to determine the presence of unit root in the series, and hence help us understand if the series is stationary or not. The null and alternate hypothesis of this test are as follows:
# 
# Null hypothesis  says Data is not stationary
# Alternative hypothesis says Data is stationary
# 
# The results can be interpret as below:
# -If critical value> test_statistic than null hypothesis is rejected ie data is stationary
# -If critical value< test_statistic than null hypothesis is not rejected ie data is not stationar
# 
# There are advanced methods to check stationarity like trend stationarity,difference stationarity. To determine trend stationarity KPSS test is needed. here the results shows that  total_cust and total_cust_total-2 are not stationary at the 1%-level.
# 
# We need implemet KPSS test for the determination of stationarity trend in timeseries

# In[65]:


#kwiatkowski-Phillips-Schmidt-Shin Test
from statsmodels.tsa.stattools import kpss


# In[66]:


def kpss_test(df, col_names):
    for name in col_names:
        print ('Results of KPSS Test for {}'.format(name))
        result_test = kpss(df[name], regression='c', lags='legacy')
        result_output = pd.Series(result_test[0:3], index=['Test Statistic','p-value','Lags Used'])
        for key, val in result_test[3].items():
            result_output['Critical Value (%s)'%key] = val
        print (result_output)


# In[67]:


# kpss test for total_cust
kpss_test(df_v2, ['total_cust'])


# In[68]:


# kpss test for total_cust_t-1
kpss_test(df_v2, ['total_cust_diff'])


# In[69]:


# kpss test for total_cust
kpss_test(testing_df, testing_df.columns)


# Kwiatkowski-Phillips-Schmidt-Shin (KPSS):
# KPSS test is a statistical test to check for stationarity of a series around a deterministic trend. Like ADF test, the KPSS test is also commonly used to analyse the stationarity of a series. However, it has couple of key differences compared to the ADF test in function and in practical usage. 
# 
# Null hypothesis  says Data is stationary
# Alternative hypothesis says Data is not stationary
# 
# The results can be interpret as below:
# -If critical value < test_statistic than null hypothesis is rejected ie data is not stationary
# -If critical value >test_statistic than null hypothesis is not rejected ie data is stationar
# 

# Here to there are condition for the need of transformation based on the timeseries is difference or trend stationary.
# 
# No transformations are needed if timeseries is difference and trend stationary both
# Transformations of total_cust is needed if timeseries is not difference but it is trend stationary 
# Transformations of total_cust_total-2 is needed if timeseries is not difference as well as not trend stationary 
