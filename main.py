import requests

# I am using this free API: https://github.com/mcnaveen/Random-Words-API

def get_word_object() -> dict :
    response = requests.get("https://random-words-api.vercel.app/word")
    [word_dictionary] = response.json()
    return word_dictionary

def word(word_object: dict) -> str :
    return word_object['word'].lower()

def definition(word_object: dict) -> str :
    return word_object['definition']

def find_all(base_string: str, sub: str) -> list :
    indexes = []
    start = 0
    while start < len(base_string):
        idx = base_string.find(sub, start)
        if idx == -1 : return indexes
        indexes.append(idx)
        start = idx + 1
    return indexes

def match(current: str, answer: str, letter: str) -> str :
    if letter not in answer:
        return current
    occurences = find_all(answer, letter)
    new_current = ''
    last_idx = 0
    for idx in occurences:
        new_current += current[last_idx : idx] + letter
        last_idx = idx + 1
    new_current += current[last_idx:]
    return new_current

WORD_OBJECT = get_word_object()
answer = word(WORD_OBJECT)
answer_definition = definition(WORD_OBJECT)
