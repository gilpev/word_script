import csv
import json

def read_csv(file_path):
    csv_file =  open(file_path, 'r')
    reader = csv.reader(csv_file)
    return reader

def dump_to_json(the_dump, the_json):
    with open(the_json, 'w+') as j:
        json.dump(the_dump, j)

def load_json(the_json):
    with open(the_json, 'r') as j:
        content = json.loads(j.read())
        return content

def get_relevant_words(csv_file_path, letters = []):
    reader = read_csv(csv_file_path)
    relevant_words = []
    for row in reader:
        if (len(row[0]) > len(list(letters))) or  (check_letters(row[0], letters) == False):
            continue
        else:
            relevant_words.append(row[0])
    return relevant_words

def check_letters(row, letters):
    letters_list = list(letters)
    for letter in list(row):
        if letter not in letters_list:
            return False
        else:
            letters_list.remove(letter)
    return True

def update_words_dictionery(words_dictionery, key, words_list, the_json):
    if key in list(words_dictionery):
        pass
    else:
        words_dictionery[key] = words_list
        dump_to_json(words_dictionery, the_json)

