#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df=pd.read_csv("Downloads/bis/wb.csv")
df


# In[4]:


df.head()


# In[2]:


df.plot();


# In[3]:


df.info()


# In[5]:


columns = list(df.columns)
columns


# In[6]:


cat = list(df.select_dtypes(include=['object']).columns)
num = list(df.select_dtypes(exclude=['object']).columns)
print(f'categorical variables:  {cat}')
print(f'numerical variables:  {num}')


# In[7]:


df.nunique(axis=0)


# In[ ]:


df.plot(kind='bar');


# In[ ]:




