# from Ex05 import generate_ngram
from networkx import difference


def generate_ngram(sequence, n: int) -> list:
    ngram = []
    for idx in range(len(sequence) - n + 1):
        ngram.append(sequence[idx:idx + n])
    return ngram


def generate_bigram_sets(txt: str)->set:
    bigrams = generate_ngram(txt,n=2)
    bigram_set = set()
    for bigram in bigrams:
        bigram_set.add(bigram)
    return bigram_set

x_set = generate_bigram_sets("paraparaparadise")        
y_set = generate_bigram_sets("paragraph")

print("x_set: ",x_set)
print("y_set: ",y_set)
union_set = x_set.union(y_set)
print("union_set",union_set)
intersection_set = x_set.intersection(y_set)
print("intersection_set: ",intersection_set)
different_set = x_set.difference(y_set)
print("se" in x_set)
print("se" in y_set)