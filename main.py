import sys
import csv
import json

max_length = sys.argv[1]
csv_path = sys.argv[2]
output_path = sys.argv[3]
words_dicrionary = {}

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def input_arg():
    # max_length = sys.argv[1]
    # csv_path = sys.argv[2]
    # output_path = sys.argv[3]
    print(max_length, csv_path, output_path)

def read_csv(file_path):
    word_file = open(file_path, 'r')
    reader = csv.reader(word_file)
    for row in reader:
        if len(row[0]) > int(max_length):
            continue
        elif f'{max_length}' in words_dicrionary:
            words_dicrionary[max_length].append(row[0])
        else:
            words_dicrionary[max_length] = [row[0]]
    add_to_json(output_path)
    read_from_json(output_path)

def add_to_json(o_path):
    output_json = open(o_path, 'w+')
    json.dump(words_dicrionary, output_json)

def read_from_json(o_path):
    # with open(o_path, 'r') as j:
    #     contents = json.loads(j.read())
    #     print(contents)
    content = open(o_path)
    content_json = json.loads(content.read())
    print(content_json)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    input_arg()
    read_csv(csv_path)

