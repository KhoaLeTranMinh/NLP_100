def atomic_extract(text: str):
    words = text.replace(".","").replace(","," ").split(" ")
    map = {}
    for i,word in enumerate(words):
        if i+1 in (1,5,6,7,8,9,15,16,19):
            map[word[0]] = i+1
        else:
            map[word[0:2]] = i+1
    return map        


result = atomic_extract("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can")               
print(result)
