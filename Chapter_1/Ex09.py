import random


def typoglycemia(text: str) -> str:
    word_list = text.split(' ')
    for i, word in enumerate(word_list):
        if len(word) > 4:
            # Take every chars except first and last
            char_list = list(word)[1:-1]
            random.shuffle(char_list)  # Shuffle them
            # Join with first and last char
            word_list[i] = word[0] + ''.join(char_list) + word[-1]

    return ' '.join(word_list)


print(typoglycemia("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind "))

# Write a program with the specification:

# Receive a word sequence separated by space
# For each word in the sequence:
# If the word is no longer than four letters, keep the word unchanged
# Otherwise,
# Keep the first and last letters unchanged
# Shuffle other letters in other positions (in the middle of the word)
# Observe the result by giving a sentence, e.g., “I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind “.
