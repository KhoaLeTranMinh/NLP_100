def generate_ngram(sequence, n: int) -> list:
    ngram = []
    for idx in range(len(sequence) - n + 1):  # idx goes from 0 to len - n
        ngram.append(sequence[idx:idx + n])
    return ngram


word_bigrams = generate_ngram('I am an NLPer'.split(' '), 2)
letter_bigrams = generate_ngram(list("I am an NLPer".replace(" ", "")), 2)

print(word_bigrams)
print(letter_bigrams)

# Implement a function that obtains n-grams from a given sequence object (e.g., string and list). Use this function to obtain word bi-grams and letter bi-grams from the sentence “I am an NLPer”
