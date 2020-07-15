#!/usr/bin/env python
# coding: utf-8

# In[2]:


x = 1400000.00
y = 1.4e6

print(x == y)


# In[3]:


0.1 + 0.2 == 0.3


# In[4]:


complex(1, 2)


# In[5]:


c = 3 + 4j


# In[7]:


c.real


# In[8]:


c.imag


# In[10]:


c.conjugate()


# In[11]:


message = "welcome how are you?"


# In[12]:


len(message)


# In[13]:


result = (4 < 5)
result


# In[14]:


L=[2,4,6,8,10]


# In[15]:


len(L)


# In[17]:


L.append(12)
L


# In[18]:


L+[14,15,16]


# In[19]:


type(L)


# In[25]:


L = [2, 3, 5, 7, 11]

L[0]


# In[26]:


t=(1,2,3,4,5)
print(t)


# In[27]:


len(t)


# In[28]:


t(2)=3


# In[29]:


numbers = {'one':1, 'two':2, 'three':3,'four':4,'five':5}


# In[30]:


numbers.keys()


# In[31]:


numbers.values()


# In[32]:


numbers.items()


# In[33]:


primes = {2, 3, 5, 7}
odds = {1, 3, 5, 7, 9}


# In[34]:


primes | odds   
primes.union(odds)


# In[ ]:




