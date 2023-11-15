import requests
import json
S = requests.Session()
with open('Data/Output/Ex25-result.txt', mode='r') as f:
    data = f.read()

# print(data)
data = json.loads(data)
URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "iiprop": "url",
    "titles": "File:{}".format(data[" image_flag"])
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(json.dumps(DATA, indent=4))

Pages = DATA["query"]["pages"]

for key, value in Pages.items():
    print(value["imageinfo"][0]["url"])
