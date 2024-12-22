import requests
from pprint import pprint

def get_the_smartest_superhero() -> str:
    the_smartest_superhero = ''
    superhero_list = ["Hulk", "Captain America", "Thanos"]
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    heroes = requests.get(url).json()

    the_smartest_superhero_intelligence = 0
    for hero in heroes:
        name = hero["name"]
        intelligence = hero["powerstats"]["intelligence"]
        if name in superhero_list:
            if intelligence > the_smartest_superhero_intelligence:
                the_smartest_superhero = name
                the_smartest_superhero_intelligence = intelligence
            else:
                continue

    return the_smartest_superhero

print("The smartest superhero from Hulk, Captain America, Thanos is: " + get_the_smartest_superhero())