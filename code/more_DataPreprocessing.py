#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import numpy as np


# In[35]:


df_v2 =pd.read_csv("df_v2.csv")
df_v2.head()


# In[36]:


df_v2.describe()


# In[37]:


df_v2.isnull().sum()


# In[38]:


for col_name in df_v2.columns: 
    print(col_name)


# In[39]:


def seasons(df):
    df['season_spring'] = df['date'].apply(lambda x: 1 if '01' in x[5:7] else 1 if '02' in x[5:7] else 1 
                                                     if '03' in x[5:7] else 0)
    df['season_summer'] = df['date'].apply(lambda x: 1 if '04' in x[5:7] else 1 if '05' in x[5:7] else 1 
                                                     if '06' in x[5:7] else 0)
    df['season_fall'] = df['date'].apply(lambda x: 1 if '07' in x[5:7] else 1 if '08' in x[5:7] else 1 
                                                     if '09' in x[5:7] else 0)    
    return df


# In[40]:


#df_v2 = seasons(df_v2)
### one hot encode the feature weekday
#day_of_week_columns = pd.get_dummies(df_v2['dayOfWeek'], prefix='dayOfWeek')
#df_v2=df_v2.merge(day_of_week_columns, left_index=True, right_index=True)
#df_v2=df_v2.join(weekday_dummies, how='left')
df_v2


# In[ ]:





# In[41]:


df_v2['total_cust_log'] = np.log(df_v2['total_cust'])
df_v2['total_cust_diff'] = df_v2['total_cust_log']-df_v2['total_cust_log'].shift(periods=1, freq=None, axis=0, fill_value=0)


# In[42]:


df_v2.drop(columns=['month','dayOfWeek','datetime','date'], inplace=True)


# In[43]:


for col_name in df_v2.columns: 
    print(col_name)


# In[44]:


#df_v2.to_csv('dataset_ohe.csv', index=False)
df_v2.to_csv('dataset_catboost.csv', index=False)

