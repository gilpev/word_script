import sys
import os
import json
from helper_functions import \
    load_json, \
    get_relevant_words,\
    update_words_dictionery, \
    get_words_by_lenght

lenght = sys.argv[1]
csv_path = sys.argv[2]
output_path = sys.argv[3]

def main_func():
    if os.path.exists(f'./{output_path}') == True:
        os.remove(f'./{output_path}')
    json_content = {}
    words_by_lenght = get_words_by_lenght(csv_path, lenght)
    for word in words_by_lenght:
        words_list = get_relevant_words(csv_path, word)
        if os.path.exists(f'./{output_path}') == True:
            json_content = load_json(output_path)
        update_words_dictionery(json_content, word, words_list, output_path)
    new_json_content = load_json(output_path)
    print(json.dumps(new_json_content, indent=2, sort_keys=True))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_func()

