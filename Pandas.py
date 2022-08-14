#!/usr/bin/env python
# coding: utf-8

# ## Pandas

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv("https://raw.githubusercontent.com/Premalatha-success/Financial-Analytics-Loan-Approval-Prediction/main/loan_prediction.csv")


# In[3]:


df.head()


# In[4]:


df.head(25)


# In[5]:


df.tail()


# In[6]:


df.tail(10)


# In[7]:


df.shape


# In[10]:


df.sample(5)


# In[12]:


df.dtypes


# In[13]:


df.info()


# In[16]:


df.isnull().sum()


# In[17]:


df.describe()


# In[18]:


df.describe(include='all')


# ## Pandas

# In[19]:


import pandas as pd


# In[20]:


labels = ['a','b','c','d']


# In[21]:


list = [10,28,3,4]


# In[22]:


import numpy as np


# In[23]:


array = np.array([1,2,3,4])


# In[25]:


dict = {'w':10,'x':20,'y':30,'z':40}


# In[26]:


pd.Series(list)


# In[27]:


pd.Series(list,index=labels)


# In[30]:


pd.Series(list,labels)


# In[32]:


pd.Series(dict)


# ## Pandas Dataframe and Indexing

# In[35]:


sports1 = pd.Series(([1,2,3,4]),index = ['cricket','football','basketball','golf'])
sports1


# In[36]:


sports1['basketball']


# In[37]:


sports2 = pd.Series(([11,13,12,4]),index = ['cricket','football','baseball','golf'])
sports2


# In[38]:


sports1+sports2


# In[49]:


df1 = pd.DataFrame(np.random.rand(8,5),index='A B C D E F G H '.split(),columns='Score1 Score2 Score3 Score4 Score5'.split())
df1


# In[41]:


df1['Score3']


# In[51]:


df2 = {'ID':[101,102,103,107,176],'Name':['John','Mercy','Akash','Kavin','Lally'],'Profits':[20,30,56,27,88]}
df = pd.DataFrame(df2)
df


# In[53]:


df1['Score3']


# In[54]:


df1[['Score2','Score1','Score5']]


# In[56]:


df1['Score6'] = df1['Score1']+df1['Score2']
df1


# In[57]:


df1.drop('Score5',axis=1)


# In[58]:


df1.drop("E",axis=0)


# In[63]:


df1['Score1']


# In[ ]:




