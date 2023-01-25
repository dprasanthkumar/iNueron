#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pymongo
client = pymongo.MongoClient("mongodb+srv://Prasanth:prasanth@cluster0.kljiibr.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


# In[3]:


database = client['jan24']


# In[4]:


coll = database['expences']


# In[11]:


data ={"sjdbf":"ahsdgahs",
      "aksdgakg":"ahdgag"}


# In[12]:


coll.insert_one(data)


# In[14]:


databases=client['Jan25']


# In[15]:


col=databases['Sample']


# In[16]:


insert={"jfhjsdfh":123,
       "hsddfhsgfhk":1456,
       "ahkgdahdg":1789}


# In[17]:


col.insert_one(insert)


# In[22]:


insert1={"one":["jhafakdjh","sudfgudgf","sadugfyiagdf","audhaifg"],
        "two":"asdhgakgf"}


# In[23]:


col.insert_one(insert1)


# In[25]:


insert2=[{"one":["jhafakdjh","sudfgudgf","sadugfyiagdf","audhaifg"],
        "two":"asdhgakgf"},
          {"one":["jhafakdjh","sudfgudgf","sadugfyiagdf","audhaifg"],
        "two":"asdhgakgf"},
          {"one":["jhafakdjh","sudfgudgf","sadugfyiagdf","audhaifg"],
        "two":"asdhgakgf"},
          {"one":["jhafakdjh","sudfgudgf","sadugfyiagdf","audhaifg"],
        "two":"asdhgakgf"},
          {"one":["jhafakdjh","sudfgudgf","sadugfyiagdf","audhaifg"],
        "two":"asdhgakgf"},
          {"one":["jhafakdjh","sudfgudgf","sadugfyiagdf","audhaifg"],
        "two":"asdhgakgf"}]


# In[26]:


col.insert_many(insert2)


# In[46]:


rec =coll.find()


# In[47]:


rec


# In[48]:


for i in rec:
    print(i)


# In[49]:


from pprint import pprint
for i in rec:
    pprint(i)


# In[50]:


recc=col.find()


# In[52]:


recc


# In[54]:


from pprint import pprint
for i in recc:
    pprint(i)


# In[ ]:




