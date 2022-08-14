#!/usr/bin/env python
# coding: utf-8

# ## Numpy

# In[2]:


import numpy as np


# In[4]:


arr = np.array([1,2,3,4,5])
arr


# In[6]:


list_of_lists = np.array([[1,2,3],[4,5,6],[7,8,9]])
list_of_lists


# In[7]:


np.arange(1,20)


# In[8]:


np.arange(30)


# In[9]:


np.arange(5,30,5)


# In[10]:


np.zeros(10)


# In[11]:


np.arange(30)


# In[12]:


np.linspace(0,1,5)


# In[13]:


np.linspace(0,100)


# In[14]:


np.ones(10,int)


# In[15]:


np.linspace(0,20,10)


# In[17]:


np.linspace(0,100)


# In[18]:


np.eye(10,dtype=int)


# In[19]:


np.random.rand(2,5)


# In[23]:


np.random.randint(1,10)


# In[24]:


np.random.randint(1,10,100)


# In[28]:


np.random.randint(1,9,10)


# In[31]:


sample_array = np.arange(30)
sample_array


# In[32]:


sample_array.reshape(5,6)


# In[34]:


rand_arr = np.random.randint(0,100,20)
rand_arr


# In[35]:


rand_arr.min()


# In[38]:


rand_arr.argmin()


# In[39]:


rand_arr.argmax()


# In[41]:


samp_arr=np.arange(2,20)
samp_arr


# In[42]:


samp_arr.min()


# In[43]:


samp_arr.argmin()


# In[44]:


samp_arr.argmax()


# In[45]:


samp_arr.max()


# In[46]:


a = np.eye(5)


# In[47]:



a


# In[49]:


a = np.random.rand(2,3)
a


# In[50]:


a.T


# In[52]:


samp = np.arange(10,28)
samp


# In[53]:


samp= samp.reshape(6,3)
samp


# In[59]:


samp = samp.reshape(3,6)
samp


# In[60]:


samp[2]=100
samp


# In[62]:


samp = np.arange(10,100)
samp


# In[63]:


samp[10:17]


# In[65]:


sub_samp = samp[0:7]
sub_samp


# In[67]:


sub_samp = samp
sub_samp


# In[68]:


samp[1:4] = 1001
samp


# ## Two Dimensional array

# In[69]:


import numpy as np


# In[71]:


sample_matrix = np.array([[24,13,2,15],[15,2,54,65],[56,76,24,7]])
sample_matrix


# In[72]:


sample_matrix[2,3]


# In[73]:


sample_matrix[2][3]


# In[74]:


sample_matrix[1][2]


# In[76]:


sample_matrix[:,2]


# In[77]:


sample_matrix[2,3]


# In[78]:


sample_matrix[2,3]


# In[80]:


sample_arr =np.arange(1,31)
sample_arr


# In[82]:


sample_arr + sample_arr


# In[83]:


np.exp(sample_array)


# In[85]:


np.sqrt(sample_array)


# In[87]:


np.log(sample_array)


# In[88]:


np.max(sample_array)


# In[89]:


np.std(sample_array)


# In[90]:


np.var(sample_array)


# In[91]:


np.mean(sample_array)


# In[94]:


array = np.random.randn(3,4) ## normal distribution
array


# In[95]:


np.round(array,decimals=4)


# In[97]:


sports = np.array(['golf','cricket','fall','cricket','football'])
np.unique(sports)


# In[ ]:




