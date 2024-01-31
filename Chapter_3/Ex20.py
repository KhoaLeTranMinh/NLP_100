from cgitb import text
import json
import os

# print(os.listdir())


def extract_data():
    with open('Data/enwiki-country.json', mode='r', encoding='utf-8') as f:
        data = f.readlines()
        for line in data:
            line_json = json.loads(line)
            if (line_json['title'] == "United Kingdom"):
                return (line_json['text'], line)


data_json, data_string = extract_data()
with open('Data/Output/wiki-uk.txt', mode='w', encoding='utf-8') as f:
    f.write(data_json)
# print(data_json)
