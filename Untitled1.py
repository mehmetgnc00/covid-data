#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import pandas
import pandas as pd
# import matplotlib
import matplotlib.pyplot as plt

# CHANGE THE PATH OF THE FILE AS PER YOUR SYSTEM
# data.csv file contains the data to be plotted

# define path of the csv file containing data
file_url = 'C:\\Users\\GNC\\Downloads\\arcade-revenue-vs-cs-doctorates.csv'
df = pd.read_csv(file_url)
print(df)

# create scatterplot
groups = df.groupby('YEAR')

for name, group in groups:
    plt.plot(group.REVENUE, group.AWARDS, marker='o', linestyle='', markersize=12, label=name)

plt.legend()

# YOU CAN CHANGE/SWAP THE VALUE OF BOTH THE AXES
# YOU CAN CHANGE THE LABEL OF BOTH THE AXES

# give names to both axes
plt.xlabel("REVENUE")
plt.ylabel("AWARDS")

# show the scatter plot
plt.show()


# In[ ]:




