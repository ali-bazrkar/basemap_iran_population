import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

data = pd.read_csv('iran_cities.csv')

# figure setting
fig = plt.figure(figsize=(7.5, 6))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# basemap object
basemap = Basemap(llcrnrlon=42.,
                  llcrnrlat=24.,
                  urcrnrlon=65.,
                  urcrnrlat=40.,
                  rsphere=(6378137.00, 6356752.3142),
                  resolution='l',
                  projection='merc',
                  lat_0=10.,
                  lon_0=-20.,
                  lat_ts=20.)

basemap.drawcoastlines()
basemap.drawcountries()
basemap.fillcontinents(color='#d9d9d9', lake_color='#ffffff')

x, y = basemap(data['longitude'].values, data['latitude'].values)
scatter = basemap.scatter(x, y, s=data['population'].values / 2300, color='#f6583e', alpha=0.5)

plt.show()
