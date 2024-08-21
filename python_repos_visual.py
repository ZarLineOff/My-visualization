
import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [],[]
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_links.append(f"<a href='{repo_url}' > {repo_name} </a>")
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    labels.append(f'{owner} /br < {description}')
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
    'title': 'The most popular python-projects in github',
    'titlefont': {'size': 28},
    'xaxis': {'title': 'Projects', 'titlefont': {'size': 28}, 'tickfont': {'size':14},},
    'yaxis': {'title': 'Stars', 'titlefont': {'size': 28}, 'tickfont': {'size':14},},
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos_visual.html')