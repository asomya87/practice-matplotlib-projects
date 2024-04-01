#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[24]:


gas = pd.read_csv('gas_prices.csv')

print(gas.Year[::3]) #to get every third year

plt.title('Gas prices over time (in USD)')

plt.plot(gas.Year, gas.USA, 'b.-', label = 'USA') #got datapoints using .b-
plt.plot(gas.Year, gas.Canada, 'r.-', label = 'Canada')
plt.plot(gas.Year, gas['South Korea'], 'g.-', label = 'South Korea')
plt.plot(gas.Year, gas.Australia, 'k.-', label = 'Australia')

plt.xticks(gas.Year[::3])

plt.xlabel("Year")
plt.ylabel("US Dollars")

plt.legend()

plt.show()


# In[45]:


gas = pd.read_csv('gas_prices.csv')

print(gas.Year[::3]) #to get every third year

plt.title('Gas prices over time (in USD)')

#Option 1 to plot values
plt.plot(gas.Year, gas.USA, 'b.-', label = 'USA') #got datapoints using .b-
plt.plot(gas.Year, gas.Canada, 'r.-', label = 'Canada')
plt.plot(gas.Year, gas['South Korea'], 'g.-', label = 'South Korea')
plt.plot(gas.Year, gas.Australia, 'k.-', label = 'Australia')


for country in gas:
    if country !='Year':
        plt.plot(gas.Year, gas[country], marker='.', label=country)

plt.xticks(gas.Year[::3])

plt.xlabel("Year")
plt.ylabel("US Dollars")

plt.legend(bbox_to_anchor=(1.05, 1))


plt.show()


# In[42]:


gas = pd.read_csv('gas_prices.csv')

print(gas.Year[::3]) #to get every third year

plt.title('Gas prices over time (in USD)')

#plt.plot(gas.Year, gas.USA, 'b.-', label = 'USA') #got datapoints using .b-
#plt.plot(gas.Year, gas.Canada, 'r.-', label = 'Canada')
#plt.plot(gas.Year, gas['South Korea'], 'g.-', label = 'South Korea')
#plt.plot(gas.Year, gas.Australia, 'k.-', label = 'Australia')

#Option 2 to plot values
for country in gas:
    if country !='Year':
        plt.plot(gas.Year, gas[country], marker='.', label=country)

plt.xticks(gas.Year[::3])

plt.xlabel("Year")
plt.ylabel("US Dollars")

plt.legend(bbox_to_anchor=(1.05, 1))


plt.show()


# In[ ]:





# In[43]:


gas = pd.read_csv('gas_prices.csv')

print(gas.Year[::3]) #to get every third year

plt.title('Gas prices over time (in USD)')

#plt.plot(gas.Year, gas.USA, 'b.-', label = 'USA') #got datapoints using .b-
#plt.plot(gas.Year, gas.Canada, 'r.-', label = 'Canada')
#plt.plot(gas.Year, gas['South Korea'], 'g.-', label = 'South Korea')
#plt.plot(gas.Year, gas.Australia, 'k.-', label = 'Australia')


#Option 3 to plot values
countries_to_view=['Australia', 'USA']

for country in gas:
    if country in countries_to_view:
        plt.plot(gas.Year, gas[country], marker='.', label=country)

plt.xticks(gas.Year[::3])

plt.xlabel("Year")
plt.ylabel("US Dollars")

plt.legend(bbox_to_anchor=(1.05, 1))


plt.show()


# In[51]:


gas = pd.read_csv('gas_prices.csv')

print(gas.Year[::3]) #to get every third year

plt.title('Gas prices over time (in USD)', fontdict={'fontweight':'bold','fontsize':18})

plt.plot(gas.Year, gas.USA, 'b.-', label = 'USA') #got datapoints using .b-
plt.plot(gas.Year, gas.Canada, 'r.-', label = 'Canada')
plt.plot(gas.Year, gas['South Korea'], 'g.-', label = 'South Korea')
plt.plot(gas.Year, gas.Australia, 'k.-', label = 'Australia')

plt.xticks(gas.Year[::3].tolist()+[2011])

plt.xlabel("Year")
plt.ylabel("US Dollars")

plt.legend()

plt.savefig('Gas_prices_figure', dpi=300)

plt.show()


# In[ ]:




