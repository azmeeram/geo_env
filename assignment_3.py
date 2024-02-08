import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr

import tools

#Loading Jeddah Weather data
df_isd = tools.read_isd_csv(r'C:\Users\AZMEERAM\Downloads\41024099999.csv')

#Visualizing ISD data for Jeddah 
plot = df_isd.plot(title="ISD data for Jeddah")

plt.savefig('ISD data Jeddah',dpi=300)


df_isd['RH'] = tools.dewpoint_to_rh(df_isd['DEW'].values,df_isd['TMP'].values)

#Calculation of Heat Index
df_isd['HI'] = tools.gen_heat_index(df_isd['TMP'].values,df_isd['RH'].values)

#Highest value for HI in 2023
df_isd.max()

print(df_isd.max())

df_isd.idxmax()

print(df_isd.idxmax())

#Air Temperature observed as this moment 
df_isd.loc[["2023-08-21 10:00:00"]]

print(df_isd.loc[["2023-08-21 10:00:00"]])

df_isd.resample('D').mean()

#Resampling HI using daily data instead of hourly data 

day=df_isd.resample('D').mean()

print(day)

plt.figure(figsize=(10, 6))
plt.plot(day.index, day['HI'], marker='o', linestyle='-', color='b')
plt.title("Daily Aggregated Heat Index 2023")
plt.xlabel("Date")
plt.ylabel("Heat Index")
plt.grid(True)

plt.savefig('HI time series 2023',dpi=300)


#plt.show()
df_isd['HI'].max()
original_hi_max = df_isd['HI'].max()
print (original_hi_max)

# Projected warming
projected_warming = 3 # in degrees Celsius

# Apply projected warming to air temperature data
df_isd['TMP_projected'] = df_isd['TMP'] + projected_warming

# Recalculate Heat Index with adjusted temperature
df_isd['HI_adjusted'] = tools.gen_heat_index(df_isd['TMP_projected'].values, df_isd['RH'].values)

adjusted_hi_max = df_isd['HI_adjusted'].max()
increase_in_hi_max = adjusted_hi_max - df_isd['HI'].max()  # Assuming you have an 'HI' column in df_isd

print("Original HI max:", df_isd['HI'].max())
print("Adjusted HI max:", adjusted_hi_max)
print("Increase in HI max value:", increase_in_hi_max)


