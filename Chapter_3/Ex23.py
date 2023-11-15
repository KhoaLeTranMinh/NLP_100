import re
from Ex20 import data_json as str_in

def section_structures() -> None:
    reg = re.compile("={2,}.*={2,}")
    categories = reg.findall(str_in)
    for category in categories:
        reg_eq = re.compile("={2,}") #match all the equal signs of one side
        equals = reg_eq.findall(category) #find all the equal signs in every Category tag
        num_eq = len(equals[0]) #basically the number of equal sign in a tag
        cate_print = re.sub('={2,}', '', category) #replace the equal signs with empty
        print(cate_print, num_eq-1)


section_structures()