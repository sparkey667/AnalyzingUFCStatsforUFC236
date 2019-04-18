#!/usr/bin/env python
# coding: utf-8

# Name =  "Dheric Seney"

# # UFC Statistics for Training 
# 
# https://www.itbusiness.ca/news/former-ufc-fighter-says-data-analytics-should-be-used-in-mma/77375
# 
# Data Analytics is not used a lot in UFC. Most fighters are training for their strengths and not necessary to defeat their opponent. Using Data Science / Data Analytics, fighters could train certain styles / techniques in order to get an upper hand against their opponent
# 
# Objective: Based on the fighters who will be fighting in UFC: 236, I will analyze each fighter's past fights and predict what they will do in the incoming PPV event

# The Data set that was retrieved for this project was from http://ufcstats.com/statistics/events/completed
# The data includeds:
#     - 10 fighters fighting in the Main Card of UFC 236
#     - 5 rounds of Data
#         - if the fight did not last 5 rounds because it was a 3 round fight or a fighter was KO'd or submitted, 0's were placed for the rounds
#     - Attempts of Significant Strikes (Head, body, leg, distance, ground, cinch)
#     - Lands of Significant Stikes (Head, body, leg, distance, ground, clinch)

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv('UFC_Rounds(extra).csv')


# In[2]:


# set up csv file to jupyter and checks to see if there is stuff

print(file.columns)
# print(file.tail(17))
# print(pd.DataFrame(file))
# file.iloc[49:]


# In[3]:


# file = file.drop(file.iloc[49:],axis=0)
file = file[:-17]
print(file)


# # Main Card
# 
# The main card: (wins-losses-draws)
# 
#     Max Holloway (20 - 3 - 0) vs Dustin Poirier (24-5-0)
#     Kelvin Gastelum (16-3-0) vs Israel Adesanya (16-0-0)
#     Eryk Anders (11-3-0) vs Khalil Rountree Jr. (7-3-0)
#     Alan Jouban (16-6-0) vs Dwight Grant (9-2-0)
#     Ovince Saint Preux (23-12-0) vs Nikita Krylov (24-6-0)
# 
# 

# getFighterStats() takes an input of the fighter name and the file name. It returns a list/ dataframe of the previous fights the fighter was in and the stats from them

# In[4]:


def getFighterStats(name,file):
    fighter = file[file['Name'] == name]
    return fighter


# In[5]:


# Set's tables for each fighter

Holloway = getFighterStats('Max Holloway', file)
Poirier = getFighterStats('Dustin Poirier', file)

Gastelum = getFighterStats('Kelvin Gastelum',file)
Adesanya = getFighterStats('Israel Adesanya',file) 

Anders = getFighterStats('Eryk Anders',file) 
RountreeJr = getFighterStats('Khalil Rountree Jr.',file)

Jouban = getFighterStats('Alan Jouban',file)
Grant = getFighterStats('Dwight Grant',file) 

Preux = getFighterStats('Saint Preux',file)
Krylov = getFighterStats('Nikita Krylov',file)


# In[6]:


print(Holloway)
print(Poirier)
print(Gastelum)
print(Adesanya)
print(Anders)
print(RountreeJr)
print(Jouban)
print(Grant)
print(Preux)
print(Krylov)
# type(Poirier)


# GetRoundStats() 
#     - Input: takes two inputts: he fighter's previous fights and stats variable created from getFighterStats() and the specific round that you want the stats for
#     - Purpose: Takes the mean for each column so its one row
#     - Output: utpus the row of stats for the specified round

# In[7]:


def getRoundStats(name,r):
        if r == 1:
            roundOne = name[name.columns[3:15]]
            stats1 = np.mean(roundOne)
            return pd.DataFrame(stats1)
        elif r == 2:
            roundTwo = name[name.columns[15:27]]
            stats2 = np.mean(roundTwo)
            return pd.DataFrame(stats2)
        elif r == 3:
            roundThree = name[name.columns[27:39]]
            stats3 = np.mean(roundThree)
            return pd.DataFrame(stats3)
        elif r == 4:
            roundFour = name[name.columns[39:51]]
            stats4 = np.mean(roundFour)
            return pd.DataFrame(stats4)
        elif r == 5:
            roundFive = name[name.columns[51::]]
            stats5 = np.mean(roundFive)
            return pd.DataFrame(stats5)
        else:
            return 'choose a round between 1 to 5'


# category()
#     - input: Takes two variables. The name of the Fighter and the specific stat needed 
#             - n = normal
#             - d = distance
#             - c = clinch
#             - g = ground
#     - Purpose: takes the sum of the columns for the specific categorical stat needed. The calculation is done on landed not attempts
#     - Output: returns the total number for the categorical stat

# In[8]:


def category(name,stat):
    if stat == 'n':
        return np.sum(name[0][1:6:2]).round(1)
    elif stat == 'd':
        return np.sum(name[0][7:8:2])
    elif stat == 'c':
        return np.sum(name[0][9:10:2])
    elif stat == 'g':
        return np.sum(name[0][11::2])
    else:
        return 'wrong stat'
        


# In[9]:


H_stats = getRoundStats(Holloway,3)
print(H_stats)
# H_stats[0][9:11:2]
category(H_stats,'g')

# clinch = getClinch(H_stats,1)
# print("total", clinch)
# distance = getDistance(H_stats,1)
# print("total", distance)
# ground = getGround(H_stats,1)
# print("total", ground,)
# normal = getNormal(H_stats,1)
# print("total", normal)


# In[10]:


# labels = 'Clinch','Distance','Ground','Normal'
# sizes = [getClinch(getRoundStats(Holloway,1),1), getDistance(getRoundStats(Holloway,1),1), getGround(getRoundStats(Holloway,1),1), getNormal(getRoundStats(Holloway,1),1)]
# colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
# explode = (0, 0, 0, 0) 
 
# # Plot
# plt.pie(sizes, explode=explode, labels=labels, colors=colors,
# autopct='%1.1f%%', shadow=True, startangle=140)
 
# plt.axis('equal')
# plt.show()


# # Stats per round
# 
# This section finds specific stats per each fighter per round. After getting the stats, the stats are placed in a pie chart so a fighter can use this data to know what their opponent is most likely going to do.
# 
# The rounds calculated are rounds 1, 2, 3. Rounds 4 and 5 were left out due to not all fighters making it to 5 rounds.

# # Round 1

# Max Holloway (20 - 3 - 0) vs Dustin Poirier (24-5-0) : Round 1

# In[11]:


plt.subplot(221)
plt.title('Max Holloway Round 1')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Holloway,1),'n'),category(getRoundStats(Holloway,1),'d'),category(getRoundStats(Holloway,1),'c'),category(getRoundStats(Holloway,1),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Dustin Poirier Round 1')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Poirier,1),'n'),category(getRoundStats(Poirier,1),'d'),category(getRoundStats(Poirier ,1),'c'),category(getRoundStats(Poirier ,1),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Kelvin Gastelum (16-3-0) vs Israel Adesanya (16-0-0) : Round 1

# In[12]:


plt.subplot(221)
plt.title('Kelvin Gastelum Round 1')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Gastelum,1),'n'),category(getRoundStats(Gastelum,1),'d'),category(getRoundStats(Gastelum,1),'c'),category(getRoundStats(Gastelum,1),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Israel Adesanya Round 1')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Adesanya ,1),'n'),category(getRoundStats(Adesanya ,1),'d'),category(getRoundStats(Adesanya ,1),'c'),category(getRoundStats(Adesanya,1),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Eryk Anders (11-3-0) vs Khalil Rountree Jr. (7-3-0) : Round 1

# In[13]:


plt.subplot(221)
plt.title('Eryk Anders Round 1')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Anders,1),'n'),category(getRoundStats(Anders,1),'d'),category(getRoundStats(Anders,1),'c'),category(getRoundStats(Anders,1),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Khalil Rountree Jr Round 1')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(RountreeJr,1),'n'),category(getRoundStats(RountreeJr,1),'d'),category(getRoundStats(RountreeJr,1),'c'),category(getRoundStats(RountreeJr ,1),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Alan Jouban (16-6-0) vs Dwight Grant (9-2-0) : Round 1

# In[14]:


plt.subplot(221)
plt.title('Alan Jouban Round 1')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Jouban,1),'n'),category(getRoundStats(Jouban,1),'d'),category(getRoundStats(Jouban,1),'c'),category(getRoundStats(Jouban,1),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Dwight Grant Round 1')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Grant,1),'n'),category(getRoundStats(Grant,1),'d'),category(getRoundStats(Grant,1),'c'),category(getRoundStats(Grant,1),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Ovince Saint Preux (23-12-0) vs Nikita Krylov (24-6-0) : Round 1

# In[15]:


plt.subplot(221)
plt.title('Ovince Saint Preux Round 1')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Preux,1),'n'),category(getRoundStats(Preux,1),'d'),category(getRoundStats(Preux,1),'c'),category(getRoundStats(Preux,1),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Nikita Krylov Round 1')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Krylov,1),'n'),category(getRoundStats(Krylov,1),'d'),category(getRoundStats(Krylov,1),'c'),category(getRoundStats(Krylov,1),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# # Round 2

# Max Holloway (20 - 3 - 0) vs Dustin Poirier (24-5-0) : Round 2

# In[16]:


plt.subplot(221)
plt.title('Max Holloway Round 2')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Holloway,2),'n'),category(getRoundStats(Holloway,2),'d'),category(getRoundStats(Holloway,2),'c'),category(getRoundStats(Holloway,2),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Dustin Poirier Round 2')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Poirier,2),'n'),category(getRoundStats(Poirier,2),'d'),category(getRoundStats(Poirier ,2),'c'),category(getRoundStats(Poirier ,2),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Kelvin Gastelum (16-3-0) vs Israel Adesanya (16-0-0) : Round 2

# In[17]:


plt.subplot(221)
plt.title('Kelvin Gastelum Round 2')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Gastelum,2),'n'),category(getRoundStats(Gastelum,2),'d'),category(getRoundStats(Gastelum,2),'c'),category(getRoundStats(Gastelum,2),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Israel Adesanya Round 2')
labels ='Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Adesanya ,2),'n'),category(getRoundStats(Adesanya ,2),'d'),category(getRoundStats(Adesanya ,2),'c'),category(getRoundStats(Adesanya,2),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Eryk Anders (11-3-0) vs Khalil Rountree Jr. (7-3-0) : Round 2

# In[18]:


plt.subplot(221)
plt.title('Eryk Anders Round 2')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Anders,2),'n'),category(getRoundStats(Anders,2),'d'),category(getRoundStats(Anders,2),'c'),category(getRoundStats(Anders,2),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Khalil Rountree Jr Round 2')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(RountreeJr,2),'n'),category(getRoundStats(RountreeJr,2),'d'),category(getRoundStats(RountreeJr,2),'c'),category(getRoundStats(RountreeJr ,2),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Alan Jouban (16-6-0) vs Dwight Grant (9-2-0) : Round 2

# In[19]:


plt.subplot(221)
plt.title('Alan Jouban Round 2')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Jouban,2),'n'),category(getRoundStats(Jouban,2),'d'),category(getRoundStats(Jouban,2),'c'),category(getRoundStats(Jouban,2),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Dwight Grant Round 2')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Grant,2),'n'),category(getRoundStats(Grant,2),'d'),category(getRoundStats(Grant,2),'c'),category(getRoundStats(Grant,2),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Ovince Saint Preux (23-12-0) vs Nikita Krylov (24-6-0) : Round 2

# In[20]:


plt.subplot(221)
plt.title('Ovince Saint Preux Round 2')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Preux,2),'n'),category(getRoundStats(Preux,2),'d'),category(getRoundStats(Preux,2),'c'),category(getRoundStats(Preux,2),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Nikita Krylov Round 2')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Krylov,2),'n'),category(getRoundStats(Krylov,2),'d'),category(getRoundStats(Krylov,2),'c'),category(getRoundStats(Krylov,2),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# # Round 3

# Max Holloway (20 - 3 - 0) vs Dustin Poirier (24-5-0) : Round 3

# In[21]:


plt.subplot(221)
plt.title('Max Holloway Round 3')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Holloway,3),'n'),category(getRoundStats(Holloway,3),'d'),category(getRoundStats(Holloway,3),'c'),category(getRoundStats(Holloway,3),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Dustin Poirier Round 3')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Poirier,3),'n'),category(getRoundStats(Poirier,3),'d'),category(getRoundStats(Poirier ,3),'c'),category(getRoundStats(Poirier ,3),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Kelvin Gastelum (16-3-0) vs Israel Adesanya (16-0-0) : Round 3

# In[22]:


plt.subplot(221)
plt.title('Kelvin Gastelum Round 3')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Gastelum,3),'n'),category(getRoundStats(Gastelum,3),'d'),category(getRoundStats(Gastelum,3),'c'),category(getRoundStats(Gastelum,3),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Israel Adesanya Round 3')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Adesanya ,3),'n'),category(getRoundStats(Adesanya ,3),'d'),category(getRoundStats(Adesanya ,3),'c'),category(getRoundStats(Adesanya,3),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Eryk Anders (11-3-0) vs Khalil Rountree Jr. (7-3-0) : Round 3

# In[23]:


plt.subplot(221)
plt.title('Eryk Anders Round 3')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Anders,3),'n'),category(getRoundStats(Anders,3),'d'),category(getRoundStats(Anders,3),'c'),category(getRoundStats(Anders,3),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Khalil Rountree Jr Round 3')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(RountreeJr,3),'n'),category(getRoundStats(RountreeJr,3),'d'),category(getRoundStats(RountreeJr,3),'c'),category(getRoundStats(RountreeJr ,3),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Alan Jouban (16-6-0) vs Dwight Grant (9-2-0) : Round 3

# In[24]:


plt.subplot(221)
plt.title('Alan Jouban Round 3')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Jouban,3),'n'),category(getRoundStats(Jouban,3),'d'),category(getRoundStats(Jouban,3),'c'),category(getRoundStats(Jouban,3),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Dwight Grant Round 3')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Grant,3),'n'),category(getRoundStats(Grant,3),'d'),category(getRoundStats(Grant,3),'c'),category(getRoundStats(Grant,3),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Ovince Saint Preux (23-12-0) vs Nikita Krylov (24-6-0) : Round 3

# In[25]:


plt.subplot(221)
plt.title('Ovince Saint Preux Round 3')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Preux,3),'n'),category(getRoundStats(Preux,3),'d'),category(getRoundStats(Preux,3),'c'),category(getRoundStats(Preux,3),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Nikita Krylov Round 3')
labels = 'Normal', 'Clinch','Distance','Ground'
sizes = [category(getRoundStats(Krylov,3),'n'),category(getRoundStats(Krylov,3),'d'),category(getRoundStats(Krylov,3),'c'),category(getRoundStats(Krylov,3),'g')]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# # Totals
# 
# Instead of getting statistics per round. Totals sums up all the stats per round to make the data into one. Once the data is gathered, More pie charts are made for comparison between opponents

# In[26]:


# Holloway
HNormal = (category(getRoundStats(Holloway,1),'n') + category(getRoundStats(Holloway,2),'n') + category(getRoundStats(Holloway,3),'n')).round(1)
HDistance =  (category(getRoundStats(Holloway,1),'d') + category(getRoundStats(Holloway,2),'d') + category(getRoundStats(Holloway,3),'d')).round(1)
HClinch =  (category(getRoundStats(Holloway,1),'c') + category(getRoundStats(Holloway,2),'c') + category(getRoundStats(Holloway,3),'c')).round(1)
HGround =  (category(getRoundStats(Holloway,1),'g') + category(getRoundStats(Holloway,2),'g') + category(getRoundStats(Holloway,3),'g')).round(1)

print(HNormal,HDistance,HClinch,HGround)


# Poirier
PNormal = (category(getRoundStats(Poirier,1),'n') + category(getRoundStats(Poirier,2),'n') + category(getRoundStats(Poirier ,3),'n')).round(1)
PDistance = (category(getRoundStats(Poirier,1),'d') + category(getRoundStats(Poirier,2),'d') + category(getRoundStats(Poirier ,3),'d')).round(1)
PClinch = (category(getRoundStats(Poirier,1),'c') + category(getRoundStats(Poirier,2),'c') + category(getRoundStats(Poirier ,3),'c')).round(1)
PGround = (category(getRoundStats(Poirier,1),'g') + category(getRoundStats(Poirier,2),'g') + category(getRoundStats(Poirier ,3),'g')).round(1)

print(PNormal,PDistance,PClinch,PGround)

# Gastelum
GNormal = (category(getRoundStats(Gastelum,1),'n') + category(getRoundStats(Gastelum,2),'n') + category(getRoundStats(Gastelum,3),'n')).round(1)
GDistance = (category(getRoundStats(Gastelum,1),'d') + category(getRoundStats(Gastelum,2),'d') + category(getRoundStats(Gastelum,3),'d')).round(1)
GClinch = (category(getRoundStats(Gastelum,1),'c') + category(getRoundStats(Gastelum,2),'c') + category(getRoundStats(Gastelum,3),'c')).round(1)
GGround = (category(getRoundStats(Gastelum,1),'g') + category(getRoundStats(Gastelum,2),'g') + category(getRoundStats(Gastelum,3),'g')).round(1)

# Adesanya
ANormal = (category(getRoundStats(Adesanya ,1),'n') + category(getRoundStats(Adesanya ,2),'n') + category(getRoundStats(Adesanya ,3),'n')).round(1)
ADistance = (category(getRoundStats(Adesanya ,1),'d') + category(getRoundStats(Adesanya ,2),'d') + category(getRoundStats(Adesanya ,3),'d')).round(1)
AClinch = (category(getRoundStats(Adesanya ,1),'c') + category(getRoundStats(Adesanya ,2),'c') + category(getRoundStats(Adesanya ,3),'c')).round(1)
AGround = (category(getRoundStats(Adesanya ,1),'g') + category(getRoundStats(Adesanya ,2),'g') + category(getRoundStats(Adesanya ,3),'g')).round(1)

print(ANormal,ADistance,AClinch,AGround)

# Anders
AnNormal = (category(getRoundStats(Anders,1),'n') + category(getRoundStats(Anders,2),'n') + category(getRoundStats(Anders,3),'n')).round(1)
AnDistance = (category(getRoundStats(Anders,1),'d') + category(getRoundStats(Anders,2),'d') + category(getRoundStats(Anders,3),'d')).round(1)
AnClinch = (category(getRoundStats(Anders,1),'c') + category(getRoundStats(Anders,2),'c') + category(getRoundStats(Anders,3),'c')).round(1)
AnGround = (category(getRoundStats(Anders,1),'g') + category(getRoundStats(Anders,2),'g') + category(getRoundStats(Anders,3),'g')).round(1)

print(AnNormal,AnDistance,AnClinch,AnGround)

# RountreeJr
RNormal = (category(getRoundStats(RountreeJr,1),'n') + category(getRoundStats(RountreeJr,2),'n') + category(getRoundStats(RountreeJr,3),'n')).round(1)
RDistance = (category(getRoundStats(RountreeJr,1),'d') + category(getRoundStats(RountreeJr,2),'d') + category(getRoundStats(RountreeJr,3),'d')).round(1)
RClinch = (category(getRoundStats(RountreeJr,1),'c') + category(getRoundStats(RountreeJr,2),'c') + category(getRoundStats(RountreeJr,3),'c')).round(1)
RGround = (category(getRoundStats(RountreeJr,1),'g') + category(getRoundStats(RountreeJr,2),'g') + category(getRoundStats(RountreeJr,3),'g')).round(1)

print(RNormal,RDistance,RClinch,RGround)

# Jouban
JNormal = (category(getRoundStats(Jouban,1),'n') + category(getRoundStats(Jouban,2),'n') + category(getRoundStats(Jouban,3),'n')).round(1)
JDistance = (category(getRoundStats(Jouban,1),'d') + category(getRoundStats(Jouban,2),'d') + category(getRoundStats(Jouban,3),'d')).round(1)
JClinch = (category(getRoundStats(Jouban,1),'c') + category(getRoundStats(Jouban,2),'c') + category(getRoundStats(Jouban,3),'c')).round(1)
JGround = (category(getRoundStats(Jouban,1),'g') + category(getRoundStats(Jouban,2),'g') + category(getRoundStats(Jouban,3),'g')).round(1)

print(JNormal,JDistance,JClinch,JGround)

# Grant
GrNormal = (category(getRoundStats(Grant,1),'n') + category(getRoundStats(Grant,2),'n') + category(getRoundStats(Grant,3),'n')).round(1)
GrDistance = (category(getRoundStats(Grant,1),'d') + category(getRoundStats(Grant,2),'d') + category(getRoundStats(Grant,3),'d')).round(1)
GrClinch = (category(getRoundStats(Grant,1),'c') + category(getRoundStats(Grant,2),'c') + category(getRoundStats(Grant,3),'c')).round(1)
GrGround = (category(getRoundStats(Grant,1),'g') + category(getRoundStats(Grant,2),'g') + category(getRoundStats(Grant,3),'g')).round(1)

print(PNormal,PDistance,PClinch,PGround)

# Preux 
PrNormal = (category(getRoundStats(Preux,1),'n') + category(getRoundStats(Preux,2),'n') + category(getRoundStats(Preux,3),'n')).round(1)
PrDistance = (category(getRoundStats(Preux,1),'d') + category(getRoundStats(Preux,2),'d') + category(getRoundStats(Preux,3),'d')).round(1)
PrClinch = (category(getRoundStats(Preux,1),'c') + category(getRoundStats(Preux,2),'c') + category(getRoundStats(Preux,3),'c')).round(1)
PrGround = (category(getRoundStats(Preux,1),'g') + category(getRoundStats(Preux,2),'g') + category(getRoundStats(Preux,3),'g')).round(1)

print(PrNormal,PrDistance,PrClinch,PrGround)

# Krylov 
KNormal = (category(getRoundStats(Krylov,1),'n') + category(getRoundStats(Krylov,2),'n') + category(getRoundStats(Krylov,3),'n')).round(1)
KDistance = (category(getRoundStats(Krylov,1),'d') + category(getRoundStats(Krylov,2),'d') + category(getRoundStats(Krylov,3),'d')).round(1)
KClinch = (category(getRoundStats(Krylov,1),'c') + category(getRoundStats(Krylov,2),'c') + category(getRoundStats(Krylov,3),'c')).round(1)
KGround = (category(getRoundStats(Krylov,1),'g') + category(getRoundStats(Krylov,2),'g') + category(getRoundStats(Krylov,3),'g')).round(1)

print(KNormal,KDistance,KClinch,KGround)


# Max Holloway (20 - 3 - 0) vs Dustin Poirier (24-5-0) : Total

# In[27]:


plt.subplot(221)
plt.title('Max Holloway Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [HClinch,HDistance,HGround,HNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Dustin Poirier Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [PClinch,PDistance,PGround,PNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Kelvin Gastelum (16-3-0) vs Israel Adesanya (16-0-0) : Total

# In[28]:


plt.subplot(221)
plt.title('Kelvin Gastelum Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [GClinch, GDistance, GGround, GNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Israel Adesanya Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [AClinch, ADistance, AGround, ANormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Eryk Anders (11-3-0) vs Khalil Rountree Jr. (7-3-0) : Total

# In[29]:


plt.subplot(221)
plt.title('Eryk Anders Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [AnClinch, AnDistance, AnGround, AnNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Khalil Rountree Jr Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [RClinch, RDistance, RGround, RNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Alan Jouban (16-6-0) vs Dwight Grant (9-2-0) : Total

# In[30]:


plt.subplot(221)
plt.title('Alan Jouban Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [JClinch, JDistance, JGround, JNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Dwight Grant Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [GrClinch, GrDistance, GrGround, GrNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Ovince Saint Preux (23-12-0) vs Nikita Krylov (24-6-0) ; Total

# In[31]:


plt.subplot(221)
plt.title('Ovince Saint Preux Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [PrClinch, PrDistance, PrGround, PrNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Nikita Krylov Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [KClinch, KDistance, KGround, KNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# # Results
# 
# On April 13th, UFC 236 took place. The data from the fights were recorded into an alike table to the first table that was used. With the data, the same process was made by creating pie charts using the data.

# In[32]:


results = pd.read_csv('UFC_Winenrs.csv')
# print(results.columns)
print(results)
results = results.drop([10], axis = 0)
print(results)


# In[33]:


Results_Holloway = getFighterStats('Max Holloway', results)
Results_Poirier = getFighterStats('Dustin Poirier', results)

Results_Gastelum = getFighterStats('Kelvin Gastelum',results)
Results_Adesanya = getFighterStats('Israel Adesanya',results) 

Results_Anders = getFighterStats('Eryk Anders',results) 
Results_RountreeJr = getFighterStats('Khalil Rountree Jr.',results)

Results_Jouban = getFighterStats('Alan Jouban',results)
Results_Grant = getFighterStats('Dwight Grant',results) 

Results_Preux = getFighterStats('Saint Preux',results)
Results_Krylov = getFighterStats('Nikita Krylov',results)


# In[34]:


# Holloway
Results_HNormal = (category(getRoundStats(Results_Holloway,1),'n') + category(getRoundStats(Results_Holloway,2),'n') + category(getRoundStats(Results_Holloway,3),'n')).round(1)
Results_HDistance =  (category(getRoundStats(Results_Holloway,1),'d') + category(getRoundStats(Results_Holloway,2),'d') + category(getRoundStats(Results_Holloway,3),'d')).round(1)
Results_HClinch =  (category(getRoundStats(Results_Holloway,1),'c') + category(getRoundStats(Results_Holloway,2),'c') + category(getRoundStats(Results_Holloway,3),'c')).round(1)
Results_HGround =  (category(getRoundStats(Results_Holloway,1),'g') + category(getRoundStats(Results_Holloway,2),'g') + category(getRoundStats(Results_Holloway,3),'g')).round(1)

print(Results_HNormal,Results_HDistance,Results_HClinch,Results_HGround)


# Poirier
Results_PNormal = (category(getRoundStats(Results_Poirier,1),'n') + category(getRoundStats(Results_Poirier,2),'n') + category(getRoundStats(Results_Poirier ,3),'n')).round(1)
Results_PDistance = (category(getRoundStats(Results_Poirier,1),'d') + category(getRoundStats(Results_Poirier,2),'d') + category(getRoundStats(Results_Poirier ,3),'d')).round(1)
Results_PClinch = (category(getRoundStats(Results_Poirier,1),'c') + category(getRoundStats(Results_Poirier,2),'c') + category(getRoundStats(Results_Poirier ,3),'c')).round(1)
Results_PGround = (category(getRoundStats(Results_Poirier,1),'g') + category(getRoundStats(Results_Poirier,2),'g') + category(getRoundStats(Results_Poirier ,3),'g')).round(1)

print(Results_PNormal,Results_PDistance,Results_PClinch,Results_PGround)

# Gastelum
Results_GNormal = (category(getRoundStats(Results_Gastelum,1),'n') + category(getRoundStats(Results_Gastelum,2),'n') + category(getRoundStats(Results_Gastelum,3),'n')).round(1)
Results_GDistance = (category(getRoundStats(Results_Gastelum,1),'d') + category(getRoundStats(Results_Gastelum,2),'d') + category(getRoundStats(Results_Gastelum,3),'d')).round(1)
Results_GClinch = (category(getRoundStats(Results_Gastelum,1),'c') + category(getRoundStats(Results_Gastelum,2),'c') + category(getRoundStats(Results_Gastelum,3),'c')).round(1)
Results_GGround = (category(getRoundStats(Results_Gastelum,1),'g') + category(getRoundStats(Results_Gastelum,2),'g') + category(getRoundStats(Results_Gastelum,3),'g')).round(1)

print(Results_GNormal,Results_GDistance,Results_GClinch,Results_GGround)

# Adesanya
Results_ANormal = (category(getRoundStats(Results_Adesanya ,1),'n') + category(getRoundStats(Results_Adesanya ,2),'n') + category(getRoundStats(Results_Adesanya ,3),'n')).round(1)
Results_ADistance = (category(getRoundStats(Results_Adesanya ,1),'d') + category(getRoundStats(Results_Adesanya ,2),'d') + category(getRoundStats(Results_Adesanya ,3),'d')).round(1)
Results_AClinch = (category(getRoundStats(Results_Adesanya ,1),'c') + category(getRoundStats(Results_Adesanya ,2),'c') + category(getRoundStats(Results_Adesanya ,3),'c')).round(1)
Results_AGround = (category(getRoundStats(Results_Adesanya ,1),'g') + category(getRoundStats(Results_Adesanya ,2),'g') + category(getRoundStats(Results_Adesanya ,3),'g')).round(1)

print(Results_ANormal,Results_ADistance,Results_AClinch,Results_AGround)

# Anders
Results_AnNormal = (category(getRoundStats(Results_Anders,1),'n') + category(getRoundStats(Results_Anders,2),'n') + category(getRoundStats(Results_Anders,3),'n')).round(1)
Results_AnDistance = (category(getRoundStats(Results_Anders,1),'d') + category(getRoundStats(Results_Anders,2),'d') + category(getRoundStats(Results_Anders,3),'d')).round(1)
Results_AnClinch = (category(getRoundStats(Results_Anders,1),'c') + category(getRoundStats(Results_Anders,2),'c') + category(getRoundStats(Results_Anders,3),'c')).round(1)
Results_AnGround = (category(getRoundStats(Results_Anders,1),'g') + category(getRoundStats(Results_Anders,2),'g') + category(getRoundStats(Results_Anders,3),'g')).round(1)

print(Results_AnNormal,Results_AnDistance,Results_AnClinch,Results_AnGround)

# RountreeJr
Results_RNormal = (category(getRoundStats(Results_RountreeJr,1),'n') + category(getRoundStats(Results_RountreeJr,2),'n') + category(getRoundStats(Results_RountreeJr,3),'n')).round(1)
Results_RDistance = (category(getRoundStats(Results_RountreeJr,1),'d') + category(getRoundStats(Results_RountreeJr,2),'d') + category(getRoundStats(Results_RountreeJr,3),'d')).round(1)
Results_RClinch = (category(getRoundStats(Results_RountreeJr,1),'c') + category(getRoundStats(Results_RountreeJr,2),'c') + category(getRoundStats(Results_RountreeJr,3),'c')).round(1)
Results_RGround = (category(getRoundStats(Results_RountreeJr,1),'g') + category(getRoundStats(Results_RountreeJr,2),'g') + category(getRoundStats(Results_RountreeJr,3),'g')).round(1)

print(Results_RNormal,Results_RDistance,Results_RClinch,Results_RGround)

# Jouban
Results_JNormal = (category(getRoundStats(Results_Jouban,1),'n') + category(getRoundStats(Results_Jouban,2),'n') + category(getRoundStats(Results_Jouban,3),'n')).round(1)
Results_JDistance = (category(getRoundStats(Results_Jouban,1),'d') + category(getRoundStats(Results_Jouban,2),'d') + category(getRoundStats(Results_Jouban,3),'d')).round(1)
Results_JClinch = (category(getRoundStats(Results_Jouban,1),'c') + category(getRoundStats(Results_Jouban,2),'c') + category(getRoundStats(Results_Jouban,3),'c')).round(1)
Results_JGround = (category(getRoundStats(Results_Jouban,1),'g') + category(getRoundStats(Results_Jouban,2),'g') + category(getRoundStats(Results_Jouban,3),'g')).round(1)

print(Results_JNormal,Results_JDistance,Results_JClinch,Results_JGround)

# Grant
Results_GrNormal = (category(getRoundStats(Results_Grant,1),'n') + category(getRoundStats(Results_Grant,2),'n') + category(getRoundStats(Results_Grant,3),'n')).round(1)
Results_GrDistance = (category(getRoundStats(Results_Grant,1),'d') + category(getRoundStats(Results_Grant,2),'d') + category(getRoundStats(Results_Grant,3),'d')).round(1)
Results_GrClinch = (category(getRoundStats(Results_Grant,1),'c') + category(getRoundStats(Results_Grant,2),'c') + category(getRoundStats(Results_Grant,3),'c')).round(1)
Results_GrGround = (category(getRoundStats(Results_Grant,1),'g') + category(getRoundStats(Results_Grant,2),'g') + category(getRoundStats(Results_Grant,3),'g')).round(1)

print(Results_PNormal,Results_PDistance,Results_PClinch,Results_PGround)

# Preux 
Results_PrNormal = (category(getRoundStats(Results_Preux,1),'n') + category(getRoundStats(Results_Preux,2),'n') + category(getRoundStats(Results_Preux,3),'n')).round(1)
Results_PrDistance = (category(getRoundStats(Results_Preux,1),'d') + category(getRoundStats(Results_Preux,2),'d') + category(getRoundStats(Results_Preux,3),'d')).round(1)
Results_PrClinch = (category(getRoundStats(Results_Preux,1),'c') + category(getRoundStats(Results_Preux,2),'c') + category(getRoundStats(Results_Preux,3),'c')).round(1)
Results_PrGround = (category(getRoundStats(Results_Preux,1),'g') + category(getRoundStats(Results_Preux,2),'g') + category(getRoundStats(Results_Preux,3),'g')).round(1)

print(Results_PrNormal,Results_PrDistance,Results_PrClinch,Results_PrGround)

# Krylov 
Results_KNormal = (category(getRoundStats(Results_Krylov,1),'n') + category(getRoundStats(Results_Krylov,2),'n') + category(getRoundStats(Results_Krylov,3),'n')).round(1)
Results_KDistance = (category(getRoundStats(Results_Krylov,1),'d') + category(getRoundStats(Results_Krylov,2),'d') + category(getRoundStats(Results_Krylov,3),'d')).round(1)
Results_KClinch = (category(getRoundStats(Results_Krylov,1),'c') + category(getRoundStats(Results_Krylov,2),'c') + category(getRoundStats(Results_Krylov,3),'c')).round(1)
Results_KGround = (category(getRoundStats(Results_Krylov,1),'g') + category(getRoundStats(Results_Krylov,2),'g') + category(getRoundStats(Results_Krylov,3),'g')).round(1)

print(Results_KNormal,Results_KDistance,Results_KClinch,Results_KGround)


# Max Holloway (20 - 3 - 0) vs Dustin Poirier (24-5-0) : Results

# In[35]:


plt.subplot(221)
plt.title('Max Holloway Results')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_HClinch,Results_HDistance,Results_HGround,Results_HNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Dustin Poirier Results')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_PClinch,Results_PDistance,Results_PGround,Results_PNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Kelvin Gastelum (16-3-0) vs Israel Adesanya (16-0-0) : Result

# In[36]:


plt.subplot(221)
plt.title('Kelvin Gastelum Results')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_GClinch, Results_GDistance, Results_GGround, Results_GNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Israel Adesanya Results')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_AClinch, Results_ADistance, Results_AGround, Results_ANormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Eryk Anders (11-3-0) vs Khalil Rountree Jr. (7-3-0) : Result

# In[37]:


plt.subplot(221)
plt.title('Eryk Anders Results')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_AnClinch, Results_AnDistance, Results_AnGround, Results_AnNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Khalil Rountree Jr Results')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_RClinch, Results_RDistance, Results_RGround, Results_RNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Alan Jouban (16-6-0) vs Dwight Grant (9-2-0) ; Result

# In[38]:


plt.subplot(221)
plt.title('Alan Jouban Results')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_JClinch, Results_JDistance, Results_JGround, Results_JNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Dwight Grant Results')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_GrClinch, Results_GrDistance, Results_GrGround, Results_GrNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# Ovince Saint Preux (23-12-0) vs Nikita Krylov (24-6-0) : Result

# In[39]:


plt.subplot(221)
plt.title('Ovince Saint Preux Results')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_PrClinch, Results_PrDistance, Results_PrGround, Results_PrNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Nikita Krylov Results')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_KClinch, Results_KDistance, Results_KGround, Results_KNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# # Comparing Total vs Result
# 
# This section compares the results I found using the methods and made vs the results of UFC 236

# ## Max Holloway 

# In[40]:


plt.subplot(221)
plt.title('Max Holloway Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [HClinch,HDistance,HGround,HNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Max Holloway Results')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_HClinch,Results_HDistance,Results_HGround,Results_HNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# ## Dustin Poirier 

# In[41]:


plt.subplot(221)
plt.title('Dustin Poirier Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [PClinch,PDistance,PGround,PNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Dustin Poirier Result')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_PClinch,Results_PDistance,Results_PGround,Results_PNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# ## Kelvin Gastelum

# In[42]:


plt.subplot(221)
plt.title('kelvin Gastelum Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [GClinch, GDistance, GGround, GNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Kevin Gastelum Result')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_GClinch, Results_GDistance, Results_GGround, Results_GNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# ## Israel Adesanya

# In[43]:


plt.subplot(221)
plt.title('Israel Adesanya Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [AClinch, ADistance, AGround, ANormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Israel Adesanya Results')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_AClinch, Results_ADistance, Results_AGround, Results_ANormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# ## Eryk Anders

# In[44]:


plt.subplot(221)
plt.title('Eryk Anders Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [AnClinch, AnDistance, AnGround, AnNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Eryk Anders')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_AnClinch, Results_AnDistance, Results_AnGround, Results_AnNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# ## Khalil Rountree Jr.

# In[45]:


plt.subplot(221)
plt.title('Khalil Rountree Jr. Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [RClinch, RDistance, RGround, RNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Khalil Rountree Jr. Result')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_RClinch, Results_RDistance, Results_RGround, Results_RNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# ## Alan Jouban

# In[46]:


plt.subplot(221)
plt.title('Alan Jouban Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [JClinch, JDistance, JGround, JNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Alan Jouban Results')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_JClinch, Results_JDistance, Results_JGround, Results_JNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# ## Dwight Grant

# In[47]:


plt.subplot(221)
plt.title('Dwight Grant')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [GrClinch, GrDistance, GrGround, GrNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Dwight Grant Results')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_GrClinch, Results_GrDistance, Results_GrGround, Results_GrNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# ## Ovince Saint Preux

# In[48]:


plt.subplot(221)
plt.title('Ovince Saint Preux Total')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [PrClinch, PrDistance, PrGround, PrNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Ovince Saint Preux Results')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_PrClinch, Results_PrDistance, Results_PrGround, Results_PrNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# ## Nikita Krylov

# In[49]:


plt.subplot(221)
plt.title('Nikita Krylov Results')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [KClinch, KDistance, KGround, KNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.subplot(222)
plt.title('Nikita Krylov Results')
labels = 'Clinch','Distance','Ground','Normal'
sizes = [Results_KClinch, Results_KDistance, Results_KGround, Results_KNormal]
colors = ['lightsteelblue', 'yellowgreen', 'plum', 'lightcoral']
explode = (0, 0, 0, 0) 
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')

plt.figure(1)



plt.show


# In[ ]:




