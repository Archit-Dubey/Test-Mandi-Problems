from more_itertools import random_permutation

def isSorted(words, order):
    ind = {c: i for i, c in enumerate(order)}
    for a, b in zip(words, words[1:]):
        if len(a) > len(b) and a[:len(b)] == b:
            return False
        for s1, s2 in zip(a, b):
            if ind[s1] < ind[s2]:
                break
            elif ind[s1] > ind[s2]:
                return False
    return True

words = input().split()
order = input()
print(isSorted(words, order))

'''hello lad
hlabcdefgijkmnopqrstuvwxyz'''