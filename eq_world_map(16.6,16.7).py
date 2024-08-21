import json
from plotly.graph_objs import Layout, Scattergeo
from plotly import offline

filename = 'C:/Users/ivann/PycharmProjects/Data visualization/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []
for eq_data in all_eq_dicts:
    mags.append(eq_data['properties']['mag'])
    lons.append(eq_data['geometry']['coordinates'][0])
    lats.append(eq_data['geometry']['coordinates'][1])
    hover_texts.append(eq_data['properties']['title'])
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [mag * 5 for mag in mags],
        'color': mags,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Magnitube'}
    },
}]
title_graph = all_eq_data['metadata']['title']
my_layout = Layout(title='Eq world map')
offline.plot({'data': data, 'layout': my_layout}, filename = 'eq_explore_data.html')