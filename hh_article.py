import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f'Status code:{r.status_code}')

response_dict = r.json()
readable_file = 'C:/Users/ivann/PycharmProjects/Data visualization/normal_hh.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)