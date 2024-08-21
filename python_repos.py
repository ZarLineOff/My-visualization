import requests
# Создание вызова API и сохранение ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=start'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')
# Сохранение ответа API в переменной
response_dict = r.json()
# Обработка результатов
print(f"Total repositories: {response_dict['total_count']}")
# Анализ информации о репозиториях
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

print(f'\nSelected information about each repository:')
for repo_dict in repo_dicts:
    print(f'Name: {repo_dict["name"]}')
    print(f'Owner: {repo_dict["owner"]["login"]}')
    print(f'Starts: {repo_dict["stargazers_count"]}')
    print(f'Repository: {repo_dict["html_url"]}')
    print(f'Created {repo_dict["created_at"]}')
    print(f'Updates: {repo_dict["updated_at"]}')
    print(f'Description: {repo_dict["description"]}')