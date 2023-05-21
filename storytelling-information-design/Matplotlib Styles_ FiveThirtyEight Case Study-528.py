## 1. Matplotlib Styles ##

import matplotlib.pyplot as plt

style.use('ggplot')
plt.plot([2, 4, 6], [10, 15, 5])
plt.show()

style.use('default')
plt.plot([2, 4, 6], [10, 15, 5])
plt.show()

## 2. Wine Quality Dataset ##

import pandas as pd
red_wine = pd.read_csv('winequality-red.csv', sep=';')
red_corr = red_wine.corr()['quality'][:-1]

white_wine = pd.read_csv('winequality-white.csv', sep=';')
white_corr = white_wine.corr()['quality'][:-1]

## 3. FiveThirtyEight Style ##

import pandas as pd
import matplotlib.pyplot as plt

red_wine = pd.read_csv('winequality-red.csv', sep=';')
red_corr = red_wine.corr()['quality'][:-1]

white_wine = pd.read_csv('winequality-white.csv', sep=';')
white_corr = white_wine.corr()['quality'][:-1]

style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize=(9, 5))

ax.barh(white_corr.index, white_corr, left=2, height = 0.5)
ax.barh(red_corr.index, red_corr, height = 0.5)

ax.grid(visible=None)
ax.set_xticklabels([])
ax.set_yticklabels([])

plt.show()

## 4. Adding Y-tick Labels ##

style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize=(9, 5))
ax.barh(white_corr.index, white_corr, left=2, height=0.5)
ax.barh(red_corr.index, red_corr, height=0.5, left=-0.1)

ax.grid(b=False)
ax.set_yticklabels([])
ax.set_xticklabels([])

x_coords = {'Alcohol': 0.82, 'Sulphates': 0.77, 'pH': 0.91,
            'Density': 0.80, 'Total Sulfur Dioxide': 0.59,
            'Free Sulfur Dioxide': 0.6, 'Chlorides': 0.77,
            'Residual Sugar': 0.67, 'Citric Acid': 0.76,
            'Volatile Acidity': 0.67, 'Fixed Acidity': 0.71}
y_coord = 9.8
for y_label, x_coord in x_coords.items():
    ax.text(x_coord, y_coord, y_label)
    y_coord -= 1
ax.axvline(0.5, c='grey', alpha=0.1, linewidth=1,
           ymin=0.1, ymax=0.9)
ax.axvline(1.45, c='grey', alpha=0.1, linewidth=1,
           ymin=0.1, ymax=0.9)
plt.show()

## 5. Adding X-tick Labels ##

style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize=(9, 5))
ax.barh(white_corr.index, white_corr, left=2, height=0.5)
ax.barh(red_corr.index, red_corr, height=0.5, left=-0.1)

ax.grid(b=False)
ax.set_yticklabels([])
ax.set_xticklabels([])

x_coords = {'Alcohol': 0.82, 'Sulphates': 0.77, 'pH': 0.91,
            'Density': 0.80, 'Total Sulfur Dioxide': 0.59,
            'Free Sulfur Dioxide': 0.6, 'Chlorides': 0.77,
            'Residual Sugar': 0.67, 'Citric Acid': 0.76,
            'Volatile Acidity': 0.67, 'Fixed Acidity': 0.71}
y_coord = 9.8
for y_label, x_coord in x_coords.items():
    ax.text(x_coord, y_coord, y_label)
    y_coord -= 1
    
ax.axvline(0.5, c='grey', alpha=0.1, linewidth=1,
           ymin=0.1, ymax=0.9)
ax.axvline(1.45, c='grey', alpha=0.1, linewidth=1,
           ymin=0.1, ymax=0.9)
ax.text(-0.33, 11.2, 'RED WINE', weight='bold')

ax.axhline(11, color='grey', linewidth=1, alpha=0.5,
          xmin=0.67, xmax=0.98)
ax.axhline(-1, color='grey', linewidth=1, alpha=0.5,
          xmin=0.01, xmax=0.32)
ax.text(1.75, 11.2, 'WHITE WINE', weight='bold')

ax.text(-0.7, -1.7, '-0.5'+ ' '*31 + '+0.5',
        color='grey', alpha=0.5)
ax.axhline(-1, color='grey', linewidth=1, alpha=0.5,
           xmin=0.67, xmax=0.98)
ax.axhline(11, color='grey', linewidth=1, alpha=0.5,
          xmin=0.01, xmax=0.32)
ax.text(1.43, -1.7, '-0.5'+ ' '*31 + '+0.5',
        color='grey', alpha=0.5)

plt.show()

## 6. Adding a Signature ##

style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize=(9, 5))
ax.barh(white_corr.index, white_corr, left=2, height=0.5)
ax.barh(red_corr.index, red_corr, height=0.5, left=-0.1)

ax.grid(b=False)
ax.set_yticklabels([])
ax.set_xticklabels([])

x_coords = {'Alcohol': 0.82, 'Sulphates': 0.77, 'pH': 0.91,
            'Density': 0.80, 'Total Sulfur Dioxide': 0.59,
            'Free Sulfur Dioxide': 0.6, 'Chlorides': 0.77,
            'Residual Sugar': 0.67, 'Citric Acid': 0.76,
            'Volatile Acidity': 0.67, 'Fixed Acidity': 0.71}
y_coord = 9.8
for y_label, x_coord in x_coords.items():
    ax.text(x_coord, y_coord, y_label)
    y_coord -= 1
    
ax.axvline(0.5, c='grey', alpha=0.1, linewidth=1,
           ymin=0.1, ymax=0.9)
ax.axvline(1.45, c='grey', alpha=0.1, linewidth=1,
           ymin=0.1, ymax=0.9)

ax.axhline(-1, color='grey', linewidth=1, alpha=0.5,
          xmin=0.01, xmax=0.32)
ax.text(-0.7, -1.7, '-0.5'+ ' '*31 + '+0.5',
        color='grey', alpha=0.5)
ax.axhline(-1, color='grey', linewidth=1, alpha=0.5,
           xmin=0.67, xmax=0.98)
ax.text(1.43, -1.7, '-0.5'+ ' '*31 + '+0.5',
        color='grey', alpha=0.5)

ax.axhline(11, color='grey', linewidth=1, alpha=0.5,
           xmin=0.01, xmax=0.32)
ax.text(-0.33, 11.2, 'RED WINE', weight='bold')
ax.axhline(11, color='grey', linewidth=1, alpha=0.5,
           xmin=0.67, xmax=0.98)
ax.text(1.75, 11.2, 'WHITE WINE', weight='bold')

ax.text(-0.7, -2.9,
        '©DATAQUEST' + ' '*94 + 'Source: P. Cortez et al.',
        color = '#f0f0f0', backgroundcolor = '#4d4d4d',
        size=12)

ax.text(-0.7, 13.5, 'Wine Quality Most Strongly Correlated With Alcohol Level', size=17, weight='bold')
ax.text(-0.7, 12.7, 'Correlation values between wine quality and wine properties (alcohol, pH, etc.)')

plt.show()

## 7. Coloring Bars Differently ##

positive_white = white_corr >= 0
color_map_white = positive_white.map({True:'#33A1C9', False:'#ffae42'})

positive_red = red_corr >= 0
color_map_red = positive_red.map({True:'#33A1C9',
                                  False:'#ffae42'})

style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize=(9, 5))
ax.barh(white_corr.index, white_corr, left=2, height=0.5,
        color=color_map_white)
ax.barh(red_corr.index, red_corr, height=0.5, left=-0.1,
        color=color_map_red)

ax.grid(b=False)
ax.set_yticklabels([])
ax.set_xticklabels([])

x_coords = {'Alcohol': 0.82, 'Sulphates': 0.77, 'pH': 0.91,
            'Density': 0.80, 'Total Sulfur Dioxide': 0.59,
            'Free Sulfur Dioxide': 0.6, 'Chlorides': 0.77,
            'Residual Sugar': 0.67, 'Citric Acid': 0.76,
            'Volatile Acidity': 0.67, 'Fixed Acidity': 0.71}
y_coord = 9.8

for y_label, x_coord in x_coords.items():
    ax.text(x_coord, y_coord, y_label)
    y_coord -= 1
    
ax.axvline(0.5, c='grey', alpha=0.1, linewidth=1,
           ymin=0.1, ymax=0.9)
ax.axvline(1.45, c='grey', alpha=0.1, linewidth=1,
           ymin=0.1, ymax=0.9)

ax.axhline(-1, color='grey', linewidth=1, alpha=0.5,
          xmin=0.01, xmax=0.32)
ax.text(-0.7, -1.7, '-0.5'+ ' '*31 + '+0.5',
        color='grey', alpha=0.5)

ax.axhline(-1, color='grey', linewidth=1, alpha=0.5,
           xmin=0.67, xmax=0.98)
ax.text(1.43, -1.7, '-0.5'+ ' '*31 + '+0.5',
        color='grey', alpha=0.5)

ax.axhline(11, color='grey', linewidth=1, alpha=0.5,
          xmin=0.01, xmax=0.32)
ax.text(-0.33, 11.2, 'RED WINE', weight='bold')

ax.axhline(11, color='grey', linewidth=1, alpha=0.5,
          xmin=0.67, xmax=0.98)
ax.text(1.75, 11.2, 'WHITE WINE', weight='bold')

ax.text(-0.7, -2.9, '©DATAQUEST' + ' '*92 + 'Source: P. Cortez et al.',
        color = '#f0f0f0', backgroundcolor = '#4d4d4d',
       size=12)

ax.text(-0.7, 13.5,
        'Wine Quality Most Strongly Correlated With Alcohol Level',
        size=17, weight='bold')
ax.text(-0.7, 12.7,
        'Correlation values between wine quality and wine properties (alcohol, pH, etc.)')

plt.show()