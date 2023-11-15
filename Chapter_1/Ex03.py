text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"
string_lists = text.split(" ")
print(string_lists)
word_lengths = []
for word in string_lists:
    length = len(word)
    word_lengths.append(length)
print(word_lengths)    