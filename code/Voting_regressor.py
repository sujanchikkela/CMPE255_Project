#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.ensemble import VotingRegressor
import matplotlib.pyplot as plt
import xgboost
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingRegressor


# In[3]:


df_v3=pd.read_csv("dataset_ohe.csv")
df_v3.head()


# In[4]:


X=df_v3.iloc[:,:]
X.drop(columns='total_cust')
y=pd.DataFrame(data=df_v3["total_cust"])


# In[5]:


#X=X.drop(columns=['total_cust','datetime','date','dayOfWeek','month'])


# In[6]:


X['year'].unique()


# In[7]:


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 100)


# In[8]:


x_array=X_train.values


# In[10]:


reg1 = GradientBoostingRegressor(random_state=1)
reg2 = RandomForestRegressor(random_state=1)
reg3 = LinearRegression()
ereg = VotingRegressor(estimators=[('gb', reg1), ('rf', reg2), ('lr', reg3)])
ereg = ereg.fit(X_train, y_train)


# In[11]:


y_train_pred = ereg.predict(X_train)


# In[12]:


y_train.info()
y_train


# In[13]:


df_v3.columns


# In[14]:


rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
rmsle = np.sqrt(mean_squared_log_error(y_train, y_train_pred))
mae = mean_absolute_error(y_train, y_train_pred)

list_scores = []
list_scores.extend([rmse, rmsle, mae])


# In[15]:


list_scores


# 
