import pandas as pd
import geopandas as gp 
from geopandas import GeoDataFrame
from shapely.geometry import Point 
import fiona
from os import listdir

replace_string = input('You will need to rename these files. Which part of the filename should be replaced?\n')

new_filename = input('What would you like it replaced with?\n')

for text_file in listdir('.'):
    if text_file.endswith('.py') | text_file.startswith('.'):
        pass
    else:
        
        print('converting ' + text_file)
        gcps = pd.read_csv(text_file)

        geometry = [Point(xy) for xy in zip(gcps.mapX, gcps.mapY)]
        crs = {'init': 'epsg:3857'}

        geo_df = GeoDataFrame(gcps, crs=crs, geometry=geometry)

        #print(geo_df.crs)

        points_4326 = geo_df.to_crs({'init': 'epsg:4326'})

        #print(points_4326.geometry[0].x)

        points_4326.mapX = [point.x for point in points_4326.geometry]
        points_4326.mapY = [point.y for point in points_4326.geometry]
        points_4326.enable = points_4326['enable'].astype(int)

        #print(points_4326)
        #data = pd.DataFrame(mapX: points_4326.map)

        new_fn = text_file.replace(replace_string, new_filename)
        points_4326.to_file(new_fn, driver="CSV")
