## 2. Graphs ##

x_unit_length = 10
y_unit_length = 1000
x_coordinate_A = 70
y_coordinate_B = 5000
C_coordinates = [50,9000]

## 3. Line Graphs ##

sentence_1 = True
sentence_2 = False
sentence_3 = True
sentence_4 = True

## 4. Matplotlib ##

import matplotlib.pyplot as plt

month_number = [1, 2, 3, 4, 5, 6, 7]
new_deaths = [213, 2729, 37718, 184064, 143119, 136073, 165003]

plt.plot(month_number, new_deaths)
plt.show()

## 5. Customizing a Graph ##

import matplotlib.pyplot as plt

month_number = [1, 2, 3, 4, 5, 6, 7]
new_deaths = [213, 2729, 37718, 184064, 143119, 136073, 165003]

plt.plot(month_number, new_deaths)
plt.ticklabel_format(axis='y',style='plain')
plt.title('New Reported Deaths By Month (Globally)')
plt.xlabel('Month Number')
plt.ylabel('Number Of Deaths')
plt.show()

## 6. WHO Time Series Data ##

import pandas as pd

WHO_time_series = pd.read_csv('WHO_time_series.csv')

WHO_time_series['Date_reported'] = pd.to_datetime(WHO_time_series['Date_reported'])

print(WHO_time_series.head(5))
print(WHO_time_series.tail(5))
      
print(WHO_time_series.info())

## 7. Types of Growth ##

def plot_cumulative_cases(country_name):
    country = who_time_series[who_time_series['Country'] == country_name]
    plt.plot(country['Date_reported'], country['Cumulative_cases'])
    plt.title('{}: Cumulative Reported Cases'.format(country_name))
    plt.xlabel('Date')
    plt.ylabel('Number of Cases')
    plt.show()

plot_cumulative_cases('Brazil')
plot_cumulative_cases('Iceland')
plot_cumulative_cases('Argentina')

brazil = 'exponential'
iceland = 'logarithmic'
argentina = 'exponential'

## 9. Comparing Line Graphs ##

france = who_time_series[who_time_series['Country'] == 'France']
uk = who_time_series[who_time_series['Country'] == 'The United Kingdom']
italy = who_time_series[who_time_series['Country'] == 'Italy']

plt.plot(france['Date_reported'], france['Cumulative_cases'],
         label='France')
plt.plot(uk['Date_reported'], uk['Cumulative_cases'],
         label='The UK')
plt.plot(italy['Date_reported'], italy['Cumulative_cases'],
         label='Italy')
plt.legend()
plt.show()

greatest_july = 'The UK'
lowest_july = 'France'
increase_march = 'Italy'