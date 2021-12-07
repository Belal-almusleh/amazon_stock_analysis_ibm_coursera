#!/usr/bin/env python
# coding: utf-8

# In[8]:


from bs4 import BeautifulSoup as bs 
import html5lib as ht 
import pandas as pd 
import requests as rq 

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html'
html_data = rq.get(url).text


soup = bs(html_data, 'html5lib')


# In[10]:


text= soup.find('title').text
print(text)


# In[17]:


amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text 
    volume = col[5].text
    amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close,  "Volume":volume}, ignore_index=True)


# In[18]:


amazon_data.head()


# In[27]:



for col in amazon_data.columns:
    print(col)


# In[31]:


print(amazon_data.iloc[5])


# In[ ]:




