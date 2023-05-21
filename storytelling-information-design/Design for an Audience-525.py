## 2. The Familiarity Principle ##

import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')
print(top20_deathtoll)
plt.barh(top20_deathtoll['Country_Other'],
         top20_deathtoll['Total_Deaths'])
plt.show()

## 4. The OO Interface ##

import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')
fig, ax = plt.subplots()
ax.barh(top20_deathtoll['Country_Other'],top20_deathtoll['Total_Deaths'])
plt.show()

## 5. Mobile-Friendly Proportions ##

import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')
fig, ax = plt.subplots(figsize=(4.5,6))
ax.barh(top20_deathtoll['Country_Other'],top20_deathtoll['Total_Deaths'])
plt.show()

## 7. Erasing Non-Data Ink ##

import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

fig, ax = plt.subplots(figsize=(4.5, 6))
ax.barh(top20_deathtoll['Country_Other'],
         top20_deathtoll['Total_Deaths'])
for location in ['left', 'right', 'bottom', 'top']:
    ax.spines[location].set_visible(False)
ax.tick_params(bottom=False, left=False)    
plt.show()

## 8. Erasing Redundant Data-Ink ##

import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

fig, ax = plt.subplots(figsize=(4.5, 6))
ax.barh(top20_deathtoll['Country_Other'],
        top20_deathtoll['Total_Deaths'],
        height=0.45)
for location in ['left', 'right', 'bottom', 'top']:
    ax.spines[location].set_visible(False)
ax.tick_params(bottom=False, left=False)    
ax.set_xticks([0, 150000, 300000])
plt.show()

## 9. The Direction of Reading ##

import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

fig, ax = plt.subplots(figsize=(4.5, 6))
ax.barh(top20_deathtoll['Country_Other'],
        top20_deathtoll['Total_Deaths'],
        height=0.45, color='#af0b1e')
for location in ['left', 'right', 'bottom', 'top']:
    ax.spines[location].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(top=False, left=False)    
ax.tick_params(axis='x', colors='grey')
ax.set_xticks([0, 150000, 300000])
plt.show()

## 10. Title and Subtitle ##

import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

fig, ax = plt.subplots(figsize=(4.5, 6))
ax.barh(top20_deathtoll['Country_Other'],
        top20_deathtoll['Total_Deaths'],
        height=0.45, color='#af0b1e')

ax.text(x=-80000, y=23.5, s='The Death Toll Worldwide Is 1.5M+',
        size=17, weight='bold')
ax.text(x=-80000, y=22.5, s='Top 20 countries by death toll (December 2020)',size=12)

for location in ['left', 'right', 'top', 'bottom']:
    ax.spines[location].set_visible(False)
    
ax.set_xticks([0, 150000, 300000])

ax.xaxis.tick_top()
ax.tick_params(top=False, left=False)
ax.tick_params(axis='x', colors='grey')

plt.show()

## 11. Final Touches ##

import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

fig, ax = plt.subplots(figsize=(4.5, 6))
ax.barh(top20_deathtoll['Country_Other'],
        top20_deathtoll['Total_Deaths'],
        height=0.45, color='#af0b1e')
for location in ['left', 'right', 'top', 'bottom']:
    ax.spines[location].set_visible(False)
ax.set_xticks([0, 150000, 300000])
ax.xaxis.tick_top()
ax.tick_params(top=False, left=False)
ax.tick_params(axis='x', colors='grey')
ax.text(x=-80000, y=23.5,
        s='The Death Toll Worldwide Is 1.5M+',
        weight='bold', size=17)
ax.text(x=-80000, y=22.5,
        s='Top 20 countries by death toll (December 2020)',
        size=12)


# *** *** *** *** *** *** *** *** *** ***

# Solution Code
ax.set_xticklabels(['0', '150,000', '300,000'])
ax.set_yticklabels([]) # an empty list removes the labels
country_names = top20_deathtoll['Country_Other']
for i, country in zip(range(20), country_names):
    ax.text(x=-80000, y=i-0.15, s=country)
ax.axvline(x=150000, ymin=0.045, c='grey',
           alpha=0.5)

plt.show()