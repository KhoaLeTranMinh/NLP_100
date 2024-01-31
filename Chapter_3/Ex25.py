import re
from attr import field

import json
#     '^(?<=\{\{Infobox country\n).*?$(.*)^(?=\})', re.MULTILINE + re.DOTALL)
with open('Data/Output/wiki-uk.txt', mode='r', encoding='utf-8') as f:
    data = f.read()

pattern_contents = re.compile(
    '^\{\{Infobox\scountry.*?$(?:.*?)^\}\}$', re.MULTILINE + re.DOTALL)  # re.DOTALL forces . to represent any character, including the next line character \n
# re.MULTILINE forces the ^to match beginning of line and & to be end of line instead of the whole pattern\
# pattern_contents = re.compile(
contents = pattern_contents.findall(data)

pattern_fields = re.compile(
    '^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n\}\}$))', re.MULTILINE + re.DOTALL)
fields = pattern_fields.findall(contents[0])
# print(str(fields))
with open('Data/Output/Ex25-contents.json', mode='w+', encoding='utf-8') as f:
    f.write(json.dumps(contents[0], indent=4))
with open('Data/Output/Ex25-fields.json', mode='w+', encoding='utf-8') as f:
    f.write(json.dumps(str(fields), indent=4))

res = {}
keys = []
for field in fields:
    res[field[0]] = field[1]
    keys.append(field[0])

with open('Data/Output/Ex25-result.json', mode='w+', encoding='utf-8') as f:
    f.write(json.dumps((res), indent=4))
