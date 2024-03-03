
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
dset = xr.open_dataset(r"C:\Users\AZMEERAM\Downloads\ERA5_Data\download.nc")

t2m = np.array(dset.variables['t2m'])
tp = np.array(dset.variables['tp'])
latitude = np.array(dset.variables['latitude'])
longitude = np.array(dset.variables['longitude'])
time_dt = np.array(dset.variables['time'])

t2m = t2m - 273.15 
tp = tp * 1000

if t2m.ndim == 4:
    t2m = np.nanmean(t2m, axis=1)
    tp = np.nanmean(tp, axis=1)

df_era5 = pd.DataFrame(index=time_dt)
df_era5['t2m'] = t2m[:,3,2]
df_era5['tp'] = tp[:,3,2]



df_era5.plot()
plt.show()

# Resample precipitation annually and calculate the mean
annual_precip = df_era5['tp'].resample('YE').mean()*24*365.25
mean_annual_precip = np.nanmean(annual_precip)

print(mean_annual_precip)

tmin = df_era5['t2m'].resample('D').min().values
tmax = df_era5['t2m'].resample('D').max().values
tmean = df_era5['t2m'].resample('D').mean().values

lat = 22.176389  # Latitude of Wadi Murwani reservoir
doy = df_era5['t2m'].resample('D').mean().index.dayofyear

print(doy)

# Compute PE
import tools
pe = tools.hargreaves_samani_1982(tmin, tmax, tmean, lat, doy)


# Convert pe to a pandas Series
pe_series = pd.Series(data=pe, index=df_era5['t2m'].resample('D').mean().index)

# Resample PE annually and calculate the mean
annual_pe = pe_series.resample('A').mean()*365

# Print mean annual PE
print("Mean Annual Potential Evaporation:")
print(annual_pe.mean())

# Plot the PE time series
ts_index = df_era5['t2m'].resample('D').mean().index
plt.figure()
plt.plot(ts_index, pe, label='Potential Evaporation')
plt.xlabel('Time')
plt.ylabel('Potential evaporation (mm d−1)')

plt.savefig("assignment_6.3v2.png", dpi=300)
plt.show()



