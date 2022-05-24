#!/usr/bin/env python
# coding: utf-8

# In[26]:



from sklearn.datasets import load_iris, load_boston
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt
import xgboost
#from sklearn.ensemble import XGBRegressor
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_log_error
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# In[27]:


df_v3=pd.read_csv("dataset_ohe.csv")
df_v3.head()


# In[28]:


X=df_v3.iloc[:,:]
X.drop(columns='total_cust')
y=pd.DataFrame(data=df_v3["total_cust"])


# In[29]:


#X=X.drop(columns=['total_cust','datetime','date','dayOfWeek','month'])


# In[30]:


X['year'].unique()


# In[31]:


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 100)


# In[32]:


xgb_clf = xgboost.XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
       colsample_bynode=1, colsample_bytree=1, gamma=0,
       importance_type='gain', learning_rate=0.1, max_delta_step=0,
       max_depth=3, min_child_weight=1, n_estimators=100,
       n_jobs=1, nthread=None, objective='reg:linear', random_state=0,
       reg_alpha=0, reg_lambda=1, scale_pos_weight=1,subsample=1, verbosity=0)
xgb_clf.fit(X_train, y_train)


# In[33]:


y_train_pred = xgb_clf.predict(X_train)


# In[34]:


y_train.info()
y_train


# In[35]:


df_v3.columns


# In[36]:


rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
rmsle = np.sqrt(mean_squared_log_error(y_train, y_train_pred))
mae = mean_absolute_error(y_train, y_train_pred)
    
list_scores = []
list_scores.extend([rmse, rmsle, mae])


# In[37]:


list_scores


