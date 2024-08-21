import csv
from matplotlib import pyplot as plt
from datetime import datetime
from plotly.graph_objs import Layout, Scattergeo
from plotly import offline

filename = 'C:/Users/ivann/PycharmProjects/Data visualization/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    lats, lons, brights = [], [], []
    for row in reader:
        try:
            lat = float(row[0])
            lon = float(row[1])
            bright = float(row[2])
        except ValueError:
            print(f'Invalid data for {row[5]}')
        else:
            lats.append(lat)
            lons.append(lon)
            brights.append(bright)
data = [{
    'type': 'scattergeo',
    'lat': lats,
    'lon': lons,
    'text': bright,
    'marker': {
        'size': 5,
        'color': lats,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Fire'}
    },
}]
my_layout = Layout(title='Fire in the world')
fig = {'data':data, 'layout': my_layout}
offline.plot(fig, filename='16.9.html')