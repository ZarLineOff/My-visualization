import json
from plotly.graph_objs import Layout, Scattergeo
from plotly import offline

filename = 'C:/Users/ivann/PycharmProjects/Data visualization/fire_normal.json'
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []
for eq_dicts in all_eq_dicts:
    mag = mags.append(eq_dicts['properties']['mag'])
    lon = lons.append(eq_dicts['geometry']['coordinates'][0])
    lat = lats.append(eq_dicts['geometry']['coordinates'][1])
    title = hover_texts.append(eq_dicts['properties']['title'])
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Magnitube'}
    },
}]
name = all_eq_data['metadata']['title']
my_layout = Layout(title=name)
fig = {'data': data, 'layout':my_layout}
offline.plot(fig, filename="Today's earthquakes(16.8).html")