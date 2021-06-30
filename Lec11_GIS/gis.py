# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 15:47:53 2021

@author: rcuppari
"""


import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

### for custom legends
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

### geopandas, for dealing with shapefiles as Pandas dataframes
import geopandas as gpd
### contextily, for base maps
import contextily as cx

### Read in CES data
ces = gpd.read_file('data/ces3shp/CESJune2018Update_SHP/CES3June2018Update.shp')
ces

### map data
ces.plot(figsize=(12,12))

### Use "CIscoreP" column for color. This gives CES Index score as a percentile.
ces.plot(figsize=(12,12), column='CIscoreP', legend=True)

### now read in roads data
roads = gpd.read_file('data/tl_2019_06_prisecroads/tl_2019_06_prisecroads.shp')
roads.crs

### project to same projection as ces shapefile
roads = roads.to_crs(ces.crs)
roads.crs

roads.plot(figsize=(12,12))
plt.xlabel('X coordinate (m)')
plt.ylabel('Y coordinate (m)')

## get primary roads (S1100, see definitions here https://www2.census.gov/geo/pdfs/reference/mtfccs2019.pdf)
roads_prim = roads.loc[roads['MTFCC'] == 'S1100', :]
roads_prim

### plotting overlapping maps
ces.plot(figsize=(12,12), column='asthmaP', legend=True, legend_kwds={'label': "Asthma Percentile"})
roads_prim.plot(color='k', lw=1)