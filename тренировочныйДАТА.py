from die import Die
from plotly.graph_objs import Bar,Layout
from plotly import offline
die_1 = Die() # Создание 2 кубиков D6
die_2 = Die()
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    freq = results.count(value)
    frequencies.append(freq)
x_values = list(range(2,max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result', 'dtick':1}
y_axis_config = {'title': 'frequencies of result'}
my_layout = Layout(title="Results of rolling two D6 1000 times", xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='dice_visual.d6_d6.html')

from random import choice
class RandomWalk():
    def __init__(self,num_points = 5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            if x_step == 0 and y_step == 0:
                continue
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
    def get_step(self):
        direction = choice([1,-1])
        distation = choice([0,1,2,3,4])
        step = direction*distation
        return step
print(plt.style.available)





import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.style.use('fivethirtyeight')
x_values = list(range(1, 5001))
y_values = [x ** 3 for x in x_values]
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=14)
ax.set_title('Кубы чисел', fontsize=24)
ax.set_xlabel('Число', fontsize=14)
ax.set_ylabel('Число', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()





import json
from plotly.graph_objs import Layout, Scattergeo
from plotly import offline

filename = 'C:/Users/ivann/PycharmProjects/Data visualization/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicts =  all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []
for eq_dicts in all_eq_dicts:
    mag = eq_dicts['properties']['mag']
    lon = eq_dicts['geometry']['coordinates'][0]
    lat = eq_dicts['geometry']['coordinates'][1]
    title = eq_dicts['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

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
my_layout = Layout(title='Землетрясения')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')



import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_links.append(f"<a href ='{repo_url}' > {repo_name} </a>")
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f'{owner} <br /> {description}'
    labels.append(label)
# Make visualization.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(100,150,250)', 'line': {'width': 1.5, 'color': 'rgb(25,25,25)'},
    },
    'opacity': 0.6
}]
my_layout = {
    'title': 'The most popular projects',
    'titlefont': {'size': 28},
    'xaxis': {'title': 'Projects', 'titlefont': {'size': 24}, 'tickfont': {'size': 14}},
    'yaxis': {'title': 'Stars', 'titlefont': {'size': 24}, 'tickfont': {'size': 14}},
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos_visual.html')

for submission_id in submission_ids[:10]:
    url = f'https://hacker-news.firebaseio.com/v0/{submission_id}.json'
    r = requests.get(url)
    print(f'id: {submission_id}\tstatus{r.status_code}')
    response_dict = r.json()
