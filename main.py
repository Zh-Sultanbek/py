import itertools

chars = list(input())
list_of_possible_chars = list(itertools.permutations(chars))

for item in list_of_possible_chars:
    print("".join(item))
