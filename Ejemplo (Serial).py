#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
series = pd.Series([1,2,3,4,5])
print(series)


# In[2]:


series1 = pd.Series([1,2,3,4,5], index = ['a','b','c','a','c'])
print(series1)


# In[3]:


print(series[2])


# In[4]:


print(series.iloc[2])


# In[5]:


print(series1['b'])
print(series1.loc['b'])


# In[6]:


print(series1['c'])


# In[7]:


print(series[2:])


# In[10]:


dates1 = pd.date_range('20200822', periods = 12)
print(dates1)
series2 = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12])
series2.index = dates1
print(series2)

