## 1. Introduction ##

import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

plt.scatter(bike_sharing['workingday'],bike_sharing['casual'])
plt.title('Working Day Vs. Casual')
plt.show()

plt.scatter(bike_sharing['workingday'],bike_sharing['registered'])
plt.title('Working Day Vs. Registered')
plt.show()

## 2. Bar Plots ##

import matplotlib.pyplot as plt
working_days = ['Non-Working Day', 'Working Day']
registered_avg = [2959, 3978]

plt.bar(x=working_days,height=registered_avg)
plt.show()

## 3. Customizing Bar Plots ##

import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])
weekday_averages = bike_sharing.groupby('weekday').mean()[['casual', 'registered']].reset_index() # It's not essential to understand how this code works, we'll cover this in a later course

plt.bar(x=weekday_averages['weekday'],height=weekday_averages['registered'])
plt.xticks(ticks=[0, 1, 2, 3, 4, 5, 6],labels=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],rotation=30)
plt.show()

## 4. Frequency Tables ##

import matplotlib.pyplot as plt

unique_values = [1, 2, 3, 4]
weather_2011 = [226, 124, 15, 0]
weather_2012 = [237, 123, 6, 0]

plt.bar(unique_values, weather_2011)
plt.xticks(ticks=[1,2,3,4])
plt.title('Weather Patterns: 2011')
plt.ylabel('Frequency')
plt.xlabel('Unique Values')
plt.show()

plt.bar(unique_values, weather_2012)
plt.xticks(ticks=[1,2,3,4])
plt.title('Weather Patterns: 2012')
plt.ylabel('Frequency')
plt.xlabel('Unique Values')
plt.show()

## 5. Grouped Frequency Tables ##

import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

registered_freq = bike_sharing['registered'].value_counts(bins=10).sort_index()

casual_freq = bike_sharing['casual'].value_counts(bins=10).sort_index()

## 6. Histograms ##

import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

plt.hist(bike_sharing['casual'])
plt.show()

## 7. The Normal Distribution ##

sentence_1 = True
sentence_2 = False
sentence_3 = True
sentence_4 = True
sentence_5 = False

## 8. The Uniform Distribution ##

sentence_1 = True
sentence_2 = False
sentence_3 = False
sentence_4 = False