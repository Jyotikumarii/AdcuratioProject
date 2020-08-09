#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs
import requests


# In[2]:


link="https://news.ycombinator.com"
page=requests.get(link)
soup=bs(page.content,'html.parser')


# In[3]:


titles=soup.find_all('a',class_='storylink')
title_list=[]
for i in range(0,len(titles)):
    title_list.append(titles[i].get_text())


# In[4]:


score=soup.find_all('span',class_='score')
score_list=[]
for i in range(0,len(score)):
    score_list.append(score[i].get_text())


# In[5]:


url=soup.find_all('span',class_='sitestr')
url_list=[]
for i in range(0,len(url)):
    url_list.append(url[i].get_text())


# In[29]:


import pymongo
from pymongo import MongoClient
try:
    cluster=MongoClient("mongodb+srv://root:1234@cluster0.5f1k2.mongodb.net/localdb?retryWrites=true&w=majority")
    db = cluster["localdb"]
    collection=db["localdb"]
    print("Connected")
except:
    print("Not connected")


# In[30]:


l=len(url_list)
for i in range(0,l):
    temp={"title":title_list[i]}
    temp1={"URL":url_list[i],"Title":temp}
    collection.insert_one(temp1)


# In[42]:


op=collection.find()
for data in op:
    print(data)


# In[32]:


import pymongo
from pymongo import MongoClient
try:
    cluster=MongoClient("mongodb+srv://root:1234@cluster0.5f1k2.mongodb.net/localdb?retryWrites=true&w=majority")
    db = cluster["localdb"]
    collection=db["localdb1"]
    print("Connected")
except:
    print("Not connected")


# In[23]:


l=len(url_list)
for i in range(0,l):
    temp={"Title":title_list[i],"Score":score_list[i]}
    temp1={"URL":url_list[i],"Metadata":temp}
    collection.insert_one(temp1)


# In[41]:


result=collection.find()
for data in result:
    print(data)

