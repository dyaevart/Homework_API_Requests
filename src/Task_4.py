import requests
import time
from pprint import pprint

url = 'https://geocode.maps.co/reverse'
token = '6768105902c20459800410cvof22be0'

def find_uk_city(coordinates:list) -> str:
    city_list = []

    for map_point in coordinates:
        params = {
            "lat": map_point[0],
            "lon": map_point[1],
            "api_key": token
        }
        response = requests.get(url, params=params).json()
        city_list.append([response["address"]["city"], response["address"]["country"]])
        time.sleep(5)

    for city, country in city_list:
        if country == "United Kingdom":
            return city

    return "City Not Found"

print(find_uk_city([('55.7514952', '37.618153095505875'),('52.3727598', '4.8936041'),('53.4071991', '-2.99168')]))


