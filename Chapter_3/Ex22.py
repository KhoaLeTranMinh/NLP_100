import re
from Ex20 import data_json as str_in

with open('Data/Output/wiki-uk.txt', mode='r', encoding='utf-8') as f:
    data = f.read()


def extract_category_names() -> None:
    reg = re.compile("\[\[Category:.*\]\]")
    categories = reg.findall(str_in)
    # print(data)
    for category in categories:
        cate_print = re.sub('\[\[Category:', '', category)
        # 3rd param is target string to do sub
        cate_print = re.sub('\]\]', '', cate_print)
        print(cate_print)


extract_category_names()
