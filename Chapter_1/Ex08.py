def cipher(string: str) -> str:
    crypted_str = ''
    for i, char in enumerate(string):
        ascii_code = ord(char)
        if ascii_code >= 97 and ascii_code <= 122:
            crypted_str += chr(219 - ascii_code)
        else:
            crypted_str += char
    return crypted_str


print(cipher("Hey there I am Khoa"))

# Implement a function cipher that converts a given string with the specification:

# Every alphabetical lowercase letter c is converted to a letter whose ASCII code is (219 - [the ASCII code of c])
# Keep other letters unchanged
# Use this function to cipher and decipher an English message.
