import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for municipio in data['municipios']:
    nome = municipio['nome']
    laudos = municipio['laudos_ecg']
    print(f'{nome}: {laudos}')
    break