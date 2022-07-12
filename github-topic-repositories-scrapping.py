#!/usr/bin/env python
# coding: utf-8

# # github-topic-repositories-scrapping

# Pick a web-site and describe your objective

# Project Outline:
# 
# - We are going to scrape https://github.com/topics
# - We will get a list  of topics. For each topic, We will get topic title. topic page URL and topic discription.
# - For each topic, we'll grab the repo name, username, stars and repo URL
# - For each topic we'll create a CSV file in the fallowing formate:
# 
# ```
# Repo Name, Username, Stars, Repo URL
# ```

# ## Use the Request library to download web pages

# In[1]:


get_ipython().system('pip install requests --upgrade')


# In[2]:


import requests


# In[3]:


topic_url = 'https://github.com/topics'


# In[4]:


response = requests.get(topic_url) ##getting info from website


# In[5]:


response.status_code ###checking if the responce was sucessful


# In[6]:


len(response.text)


# In[7]:


page_contents = response.text


# ## Use Beautiful Soup to parse and extract information

# In[8]:


get_ipython().system('pip install beautifulsoup4 --upgrade')


# In[9]:


from bs4 import BeautifulSoup


# In[10]:


doc = BeautifulSoup(page_contents, 'html.parser')


# In[11]:


doc


# In[12]:


topic_class = 'f3 lh-condensed mb-0 mt-1 Link--primary'

topic_title_tags = doc.find_all('p', {'class' : topic_class})


# In[13]:


len(topic_title_tags)


# In[14]:


topic_title_tags


# In[16]:


disc_class = 'f5 color-fg-muted mb-0 mt-1'

topic_discription_tags = doc.find_all('p', {'class' : disc_class})


# In[17]:


len(topic_discription_tags)


# In[18]:


topic_discription_tags


# In[19]:


links_class = 'no-underline flex-grow-0'

topic_link_tags = doc.find_all('a', {'class' : links_class})


# In[20]:


len(topic_link_tags)


# In[21]:


topic_link_tags


# In[22]:


topic0_url = "https://github.com" + topic_link_tags[0]['href']
print(topic0_url)


# In[27]:


topic_titles = []

for tag in topic_title_tags:
    topic_titles.append(tag.text)

print(topic_titles)


# In[30]:


topic_discription = []

for tag in topic_discription_tags:
    topic_discription.append(tag.text.strip())
    
print(topic_discription)


# In[34]:


topic_urls = []
base_url = 'https://github.com'

for tag in topic_link_tags:
    topic_urls.append(base_url + tag['href'])

print(topic_urls)


# In[35]:


get_ipython().system('pip install pandas')


# In[36]:


import pandas as pd


# In[37]:


topic_dict = {
    'title' : topic_titles,
    'Discription' : topic_discription,
    'links' : topic_urls
}


# In[43]:


topic_df = pd.DataFrame(topic_dict)

topic_df


# ## Create CSV file(s) with extracted information

# In[47]:


topic_df.to_csv('topic.csv' ,index= None)

