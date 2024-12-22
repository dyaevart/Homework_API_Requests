import requests
from pprint import pprint


def get_the_smartest_superhero(superheros):
   the_smartest_superhero = ''
   url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
   heroes = requests.get(url).json()

   the_smartest_superhero_intelligence = 0
   for hero in heroes:
       hero_id = hero["id"]
       name = hero["name"]
       intelligence = hero["powerstats"]["intelligence"]
       if hero_id in superheros:
           if intelligence > the_smartest_superhero_intelligence:
               the_smartest_superhero = name
               the_smartest_superhero_intelligence = intelligence
           else:
               continue

   return the_smartest_superhero

print("The smartest superhero from list is: " + get_the_smartest_superhero([1,6,7]))