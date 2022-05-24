#!/usr/bin/env python
# coding: utf-8

# In[49]:


from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt
import xgboost
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# In[50]:


df_v3=pd.read_csv("dataset_ohe.csv")
df_v3.head()


# In[51]:


X=df_v3.iloc[:,:]
X.drop(columns='total_cust')
y=pd.DataFrame(data=df_v3["total_cust"])


# In[52]:


#X=X.drop(columns=['total_cust','datetime','date','dayOfWeek','month'])


# In[53]:


X['year'].unique()


# In[54]:


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 100)


# In[55]:


x_array=X_train.values


# In[57]:


gbr_clf =  GradientBoostingRegressor(n_estimators=200, max_depth=1, learning_rate=1.0,min_samples_split= 5,random_state=1)
gbr_clf.fit(X_train, y_train)


# In[58]:


y_train_pred = gbr_clf.predict(X_train)


# In[59]:


y_train.info()
y_train


# In[60]:


df_v3.columns


# In[61]:


rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
rmsle = np.sqrt(mean_squared_log_error(y_train, y_train_pred))
mae = mean_absolute_error(y_train, y_train_pred)

list_scores = []
list_scores.extend([rmse, rmsle, mae])


# In[62]:


list_scores


# 
