import sys
import os
import json
from helper_functions import \
    load_json, \
    get_relevant_words,\
    update_words_dictionery

max_length = sys.argv[1]
csv_path = sys.argv[2]
output_path = sys.argv[3]

def main_func():
    json_content = {}
    words_list = get_relevant_words(csv_path, max_length)
    if os.path.exists(f'./{output_path}') == True:
        json_content = load_json(output_path)
    update_words_dictionery(json_content, max_length, words_list, output_path)
    new_json_content = load_json(output_path)
    print(json.dumps(new_json_content, indent=2, sort_keys=True))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_func()

