#!/usr/bin/env python
# coding: utf-8

# In[8]:


from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import confusion_matrix,classification_report
import matplotlib.pyplot as plt
import xgboost
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# In[9]:


df_v3=pd.read_csv("dataset_ohe.csv")
df_v3.head()


# In[10]:


X=df_v3.iloc[:,:]
X.drop(columns='total_cust')
y=pd.DataFrame(data=df_v3["total_cust"])


# In[11]:


#X=X.drop(columns=['total_cust','datetime','date','dayOfWeek','month'])


# In[12]:


X['year'].unique()


# In[13]:


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 100)


# In[14]:


x_array=X_train.values


# In[15]:


ada_clf = AdaBoostRegressor(base_estimator=DecisionTreeRegressor(),n_estimators = 200, learning_rate = 0.5, random_state = 100)
ada_clf.fit(X_train, y_train)


# In[16]:


y_train_pred = ada_clf.predict(X_train)


# In[17]:


y_train.info()
y_train


# In[19]:


df_v3.columns


# In[20]:


rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
rmsle = np.sqrt(mean_squared_log_error(y_train, y_train_pred))
mae = mean_absolute_error(y_train, y_train_pred)
    
list_scores = []
list_scores.extend([rmse, rmsle, mae])


# In[21]:


list_scores


# 
