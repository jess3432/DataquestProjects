## 1. Bike Sharing Time Series ##

import pandas as pd

bike_sharing = pd.read_csv('day.csv')

bike_sharing.head(5)
bike_sharing.tail(5)

bike_sharing.info()

## 2. Exploring Data ##

import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

plt.plot(bike_sharing['dteday'],bike_sharing['casual'],label='Casual')
plt.plot(bike_sharing['dteday'],bike_sharing['registered'],label='Registered')
plt.xticks(rotation=30)
plt.ylabel('Bikes Rented')
plt.xlabel('Date')
plt.title('Bikes Rented: Casual vs. Registered')
plt.legend()
plt.show()

## 3. Seasonal Trends ##

import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])
plt.plot(bike_sharing['dteday'],bike_sharing['temp'])
plt.xticks(rotation='45')
plt.show()

## 4. Scatter Plots ##

import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

plt.scatter(bike_sharing['windspeed'],bike_sharing['cnt'])
plt.xlabel('Wind Speed')
plt.ylabel('Bikes Rented')
plt.show()

## 5. Correlation ##

import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

plt.scatter(bike_sharing['atemp'],bike_sharing['registered'])
plt.show()

correlation = 'positive'

## 6. Pearson Correlation Coefficient ##

sentence_1 = True
sentence_2 = True
sentence_3 = False
sentence_4 = True

## 7. Measuring Pearson's r ##

import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

temp_atemp_corr = bike_sharing['temp'].corr(bike_sharing['atemp'])
wind_hum_corr = bike_sharing['windspeed'].corr(bike_sharing['hum'])
                                               
plt.scatter(bike_sharing['temp'],bike_sharing['atemp'])
plt.xlabel('Air Temperature')
plt.ylabel('Feeling Temperature')
plt.show()
                                               
plt.scatter(bike_sharing['windspeed'],bike_sharing['hum'])
plt.xlabel('Wind Speed')
plt.ylabel('Humidity')
plt.show()

## 8. Categorical Columns ##

import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')

sentence_1 = True
sentence_2 = True
sentence_3 = True

print(bike_sharing.corr()['weathersit'][['cnt', 'hum']])