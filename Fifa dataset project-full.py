#!/usr/bin/env python
# coding: utf-8

# # Portfolio project on fifa dataset

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fifa = pd.read_csv('Fifa_data.csv')

fifa


# In[4]:


fifa = pd.read_csv('Fifa_data.csv')

fifa.head(5)


# In[11]:


#Code starts here
#We will draw a histogram

fifa = pd.read_csv('Fifa_data.csv')

#setting a range for X-axis using bins from 40 above
bins = [40,50,60,70,80,90,100]

plt.hist(fifa.Overall, bins=bins)

plt.xticks(bins)

plt.xlabel("Total number of Players")
plt.ylabel("Skill level")
plt.title("Distribution of Player Skills in FIFA 2018")


plt.show()


# In[13]:


#Code starts here to check whether any players had a score above 90 points
#We will draw a histogram

fifa = pd.read_csv('Fifa_data.csv')

#setting a range for X-axis using bins from 40 above
bins = [80,90,100]

#using colorpicker on Google to select a color
plt.hist(fifa.Overall, bins=bins, color='#f5e342')

plt.xticks(bins)

plt.xlabel("Total number of Players")
plt.ylabel("Skill level")
plt.title("Distribution of Player Skills in FIFA 2018")


plt.show()


# In[27]:


#Drawing a piechart 1 using FIFA dataset

#The display.max_columns option controls the number of columns to be printed. 
#It receives an int or None, the latter used to print all the columns):

pd.set_option('display.max_columns', None)
#fifa['Preferred Foot']
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()

left


# In[29]:


#Drawing a piechart 1 using FIFA dataset

#The display.max_columns option controls the number of columns to be printed. 
#It receives an int or None, the latter used to print all the columns):

pd.set_option('display.max_columns', None)
#fifa['Preferred Foot']
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0] #this gives us the total number of people 

left


# In[30]:


#Drawing a piechart  1 using FIFA dataset

#The display.max_columns option controls the number of columns to be printed. 
#It receives an int or None, the latter used to print all the columns):

pd.set_option('display.max_columns', None)
#fifa['Preferred Foot']
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()

right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0] #this gives us the total number of people 

right #You will find that more people prefer Right foot


# In[40]:


#Drawing a piechart 1 using FIFA dataset

#The display.max_columns option controls the number of columns to be printed. 
#It receives an int or None, the latter used to print all the columns):

pd.set_option('display.max_columns', None)
#fifa['Preferred Foot']
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0] #we need to pass this number for piechart

right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0] #we need to pass this number for piechart

labels = ['Left', 'Right']

colors = ['#f54298', '#5742f5'] #using Google's color picker

plt.pie([left,right], labels=labels, colors=colors, autopct='%0.2f%%')

plt.title('Foot Preference of FIFA Players')

plt.show()


# In[42]:


#Drawing a piechart 2 using FIFA dataset

fifa.Weight


# In[43]:


fifa.Weight = [x.strip('lbs') if type(x) == str else x for x in fifa.Weight]

fifa.Weight[0]


# In[46]:


fifa.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.Weight]

fifa.Weight[0]


# In[49]:


fifa.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.Weight]

light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa.loc[(fifa.Weight >=125) & (fifa.Weight <150)].count()[0]
medium = fifa.loc[(fifa.Weight >=150) & (fifa.Weight <175)].count()[0]
medium_heavy = fifa.loc[(fifa.Weight >=175) & (fifa.Weight <200)].count()[0]
heavy = fifa.loc[(fifa.Weight > 200)].count()[0]

heavy


# In[50]:


fifa.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.Weight]

light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa.loc[(fifa.Weight >=125) & (fifa.Weight <150)].count()[0]
medium = fifa.loc[(fifa.Weight >=150) & (fifa.Weight <175)].count()[0]
medium_heavy = fifa.loc[(fifa.Weight >=175) & (fifa.Weight <200)].count()[0]
heavy = fifa.loc[(fifa.Weight > 200)].count()[0]

medium


# In[59]:


fifa.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.Weight]

light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa.loc[(fifa.Weight >=125) & (fifa.Weight <150)].count()[0]
medium = fifa.loc[(fifa.Weight >=150) & (fifa.Weight <175)].count()[0]
medium_heavy = fifa.loc[(fifa.Weight >=175) & (fifa.Weight <200)].count()[0]
heavy = fifa.loc[(fifa.Weight > 200)].count()[0]

weights = [light, light_medium, medium, medium_heavy, heavy]
labels = ['Below 125', '125-150', '150-175', '175-200', 'Greater than 200']

plt.pie(weights, labels = labels)

plt.show()


# In[65]:


fifa.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.Weight]

#plt.style.use('default') #option1
plt.style.use('ggplot') #option2


light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa.loc[(fifa.Weight >=125) & (fifa.Weight <150)].count()[0]
medium = fifa.loc[(fifa.Weight >=150) & (fifa.Weight <175)].count()[0]
medium_heavy = fifa.loc[(fifa.Weight >=175) & (fifa.Weight <200)].count()[0]
heavy = fifa.loc[(fifa.Weight > 200)].count()[0]

weights = [light, light_medium, medium, medium_heavy, heavy]
labels = ['Below 125', '125-150', '150-175', '175-200', 'Greater than 200']
explode = (.4, .2, 0, 0, .4)

plt.title("Weight distribution of FIFA Players (in lbs)")

plt.pie(weights, labels = labels, autopct ='%.2f %%', explode=explode)

plt.show()


# In[67]:


#Drawing a histogram

plt.style.use('ggplot')

barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']

madrid


# In[74]:


#Drawing a histogram

plt.style.use('default') #option1
#plt.style.use('ggplot') #option2

plt.figure(figsize=(5,8))

barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
revs = fifa.loc[fifa.Club == 'New England Revolution']['Overall']

labels = ['FC Barcelona', 'Real Madrid', 'NE Revolution']

plt.boxplot([barcelona, madrid, revs], labels = labels)

plt.title('Professional Soccer Team Comparison')
plt.ylabel('FIFA Overall Rating')

plt.show()


# In[83]:


#Drawing a histogram

plt.style.use('default') #option1
#plt.style.use('ggplot') #option2

plt.figure(figsize=(5,8))

barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
revs = fifa.loc[fifa.Club == 'New England Revolution']['Overall']

labels = ['FC Barcelona', 'Real Madrid', 'NE Revolution']

boxes = plt.boxplot([barcelona, madrid, revs], labels = labels, patch_artist=True, medianprops={'linewidth':2})

#to change the styling of each box plot and setting edge color
for box in boxes ['boxes']:
    box.set(color='#4286f4', linewidth = 2)
    
#change fill color
    box.set(facecolor='#e0e0e0')

plt.title('Professional Soccer Team Comparison')
plt.ylabel('FIFA Overall Rating')

plt.show()


# In[ ]:




