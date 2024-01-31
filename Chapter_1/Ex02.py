def concat_each_char_1by1(str1: str, str2: str) -> str:
    output_str = ''
    for char1, char2 in zip(str1, str2):
        output_str += char1 + char2
    return output_str


result = concat_each_char_1by1("shoe","cold")
print(result)