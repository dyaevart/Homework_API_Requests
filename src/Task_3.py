import requests
from pprint import pprint

url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
token = 'dict.1.1.20241222T121220Z.c104822b50f50991.3342b698841af45db0a995c42c30a6d9c3df54ca'


def translate_word(word):
    params = {
        "key": token,
        "lang": "en-ru",
        "text": word
    }
    response = requests.get(url, params=params).json()
    trans_word = response["def"][0]["tr"][0]["text"]
    return trans_word


print("translated word = " + translate_word("car"))
