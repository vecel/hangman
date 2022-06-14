import requests


def get_word_object() -> dict :
    response = requests.get("https://random-words-api.vercel.app/word")
    [word_dictionary] = response.json()
    return word_dictionary

def word(word_object: dict) -> str :
    return word_object['word'].lower()

def definition(word_object: dict) -> str :
    return word_object['definition']
