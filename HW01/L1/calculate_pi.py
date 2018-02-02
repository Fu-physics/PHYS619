
# coding: utf-8

# In[8]:


import numpy as np


# In[9]:



ini = 0.0

for k in range(50):
    ini = ini + (-3)**(-k)/(2*k+1)
    
print ("PI is:", np.sqrt(12)*ini)


# In[11]:


data = np.loadtxt("data.csv")


# In[13]:


print("Median number is:",np.median(data))

