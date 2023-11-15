from Ex20 import result
import re
def category_line_extract():
    reg = re.compile("\[\[Category:.*")
    categories = reg.findall(result)
    for category in categories:
        print(category)

category_line_extract()        