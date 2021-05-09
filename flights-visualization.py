#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


flights = pd.read_csv('/content/flights_data.csv')
print(flights.shape)
flights.head()


# In[ ]:


sb.countplot(data = flights, x = 'Source')
#plt.xticks(rotation = 30)
plt.ylabel('Number of flights',fontsize=12)
plt.xlabel('Source',fontsize=12)


# In[ ]:


base_color = sb.color_palette()[4]
sb.countplot(data=flights, x='Source', color=base_color)
plt.xticks(rotation = 30)


# In[ ]:


base_color = sb.color_palette()[0]
gen_order = flights['Source'].value_counts().index
sb.countplot(data = flights, x= 'Source', color = base_color, order = gen_order);


# In[ ]:


base_color = sb.color_palette()[2]
sb.countplot(data = flights, x = 'Airline', color = base_color);


# In[ ]:


base_color = sb.color_palette()[2]
sb.countplot(data = flights, x = 'Airline', color = base_color)
plt.xticks(rotation = 90);


# In[ ]:


base_color = sb.color_palette()[2]
sb.countplot(data = flights, y = 'Airline', color = base_color);


# ## Count Missing Data

# In[ ]:


flights.isna().sum()


# In[ ]:


na_counts = flights.isna().sum()
base_color = sb.color_palette()[3]
sb.barplot(na_counts.index.values, na_counts, color = base_color)
plt.xticks(rotation = 90)
plt.ylabel('Number of missing values', fontsize = 12)


# # Pie Chart

# In[ ]:


sorted_counts =flights['Destination'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle=90, counterclock=False);
plt.axis('square')
plt.title('Flight Destination\'s')


# In[ ]:


sorted_counts =flights['Destination'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle=90, counterclock=False, wedgeprops={'width' : 0.4});
plt.axis('square');


# # Histograms

# In[ ]:


plt.hist(data = flights, x= 'Duration(minutes)')


# In[ ]:


plt.hist(data = flights, x= 'Price', bins=20)


# In[ ]:


bins = np.arange(0, flights['Price'].max()+1, 1200)
plt.hist(data = flights, x='Price', bins = bins)
plt.show()


# In[ ]:


sb.distplot(flights['Price']);


# In[ ]:


sb.distplot(flights['Price'], kde=False);


# In[ ]:


bin_edges = np.arange(0, flights['Price'].max()+1, 1200)
sb.distplot(flights['Price'], bins = bin_edges, kde = False, hist_kws = {'alpha':1});


# In[ ]:




