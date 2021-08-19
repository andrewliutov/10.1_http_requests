import requests


API_BASE_URL = 'https://superheroapi.com/api/2619421814940190'
hero_list = ['Hulk', 'Captain America', 'Thanos']
hero_dict = {}

for hero in hero_list:
    req = requests.get(API_BASE_URL + '/search/' + hero)
    hero_dict[hero] = int(req.json()['results'][0]['powerstats']['intelligence'])

print(f'Самый умный супергерой - {max(hero_dict,key=hero_dict.get)}')
