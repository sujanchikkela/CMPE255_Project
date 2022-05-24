#!/usr/bin/env python
# coding: utf-8

# In[4]:


from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import confusion_matrix,classification_report

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import tree
from sklearn.svm import SVR


# In[3]:


get_ipython().system('pip install catboost')
from catboost import CatBoostRegressor


# In[75]:


df_v3=pd.read_csv("dataset_ohe.csv")
df_v3.head()


# In[76]:


X=df_v3.iloc[:,:]
X.drop(columns='total_cust')
y=pd.DataFrame(data=df_v3["total_cust"])


# In[77]:


#X=X.drop(columns=['total_cust','datetime','date','dayOfWeek','month'])


# In[78]:


X['year'].unique()


# In[79]:


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 100)


# In[80]:


x_array=X_train.values


# In[81]:



model=CatBoostRegressor()
model.fit(X_train, y_train)


# In[82]:


y_train_pred = model.predict(X_train)


# In[83]:


y_train.info()
y_train


# In[84]:


df_v3.columns


# In[85]:


rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
rmsle = np.sqrt(mean_squared_log_error(y_train, y_train_pred))
mae = mean_absolute_error(y_train, y_train_pred)

list_scores = []
list_scores.extend([rmse, rmsle, mae])


# In[86]:


list_scores


# 
