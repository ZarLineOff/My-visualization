import requests
from plotly.graph_objs import Bar, Layout
from plotly import offline
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    print(f'id: {submission_id}\tStatus: {r.status_code}')
    response_dict = r.json()
    submission_dict = {
        'title': response_dict['title'],
        'hh_link': f'http://news.ycombinator.com/item?id={submission_id}',
        'comments': response_dict['descendants']
    }
    submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
title = [item['title'] for item in submission_dicts]
comment = [item['comments'] for item in submission_dicts]
data = Bar(x=title, y=comment)
my_layout = {
    'title': 'Posts',
    'xaxis': {'title': 'article'},
    'yaxis': {'title': 'Likes'}
}
offline.plot({'data': data, 'layout': my_layout}, filename='eq_data_30_day_m1.html')
