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
    ''' Find and return list of all occurences of sub in base_string '''

    indexes = []
    start = 0
    while start < len(base_string):
        idx = base_string.find(sub, start)
        if idx == -1 : return indexes
        indexes.append(idx)
        start = idx + 1
    return indexes

def match(current: str, answer: str, letter: str) -> str :
    ''' Fill the "current" word status with letter where it occurs in answer 
    
        Return updated word status '''
    
    occurences = find_all(answer, letter)
    new_current = ''
    last_idx = 0
    for idx in occurences:
        new_current += current[last_idx : idx] + letter
        last_idx = idx + 1
    new_current += current[last_idx:]
    return new_current

def take_letter() -> str :
    ''' Ask user for a letter and check if it is correct (single letter, a-z or A-Z)
        
        Return that letter if it is correct "#" otherwise'''

    char = input('Type a character: ')
    if len(char) == 1 and char.isalpha() :
        return char.lower()
    return '#'

def empty_word(string: str) -> str :
    ''' Construct string composed of "_" characters
    
        Return string that's length is same as given string's length '''

    empty = ''
    for i in string:
        empty += '_'
    return empty 

def run() -> None :
    WORD_OBJECT = get_word_object()
    answer = word(WORD_OBJECT)
    answer_definition = definition(WORD_OBJECT)
    lifes = 10

    word_status = empty_word(answer)
    print(word_status)
    while lifes > 0:
        guess = take_letter()
        if guess == '#': 
            print('Wrong input, try again')
            continue
        if guess not in answer:
            lifes -= 1
            print('No', guess, 'in answer, remaining lifes: ', lifes)
            continue

        word_status = match(word_status, answer, guess)
        print(word_status)

run()