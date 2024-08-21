import json

filename = 'Файл,где хранится словарь'
with open(filename) as f:
    all_eq_file = json.load(f)

readable_file = 'Файл,где будет хранится нормальный словарь'
with open(readable_file, 'w') as f:
    json.dump(all_eq_file, f, indent=4)