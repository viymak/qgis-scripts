import pandas as pd
import geopandas as gp 
from geopandas import GeoDataFrame
from shapely.geometry import Point 
import fiona

gcps = pd.read_csv('./brom1895bos-01-points.points.csv', usecols=['mapX', 'mapY'])

geometry = [Point(xy) for xy in zip(gcps.mapX, gcps.mapY)]
crs = {'init': 'epsg:3857'}

geo_df = GeoDataFrame(gcps, crs=crs, geometry=geometry)

#print(geo_df.crs)


points_4326 = geo_df.to_crs({'init': 'epsg:4326'})

print(points_4326.geometry[0].x)

#print(points_4326)


#points_4326.to_file('39999059011260_01.points', driver="CSV")
