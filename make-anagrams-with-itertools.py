# Run with python installed
import itertools

def get_permutations(word):
    list_permutations = list(itertools.permutations(word))
    res = []
    for i in list_permutations:
       anagram = ''.join(i)
       res.append(anagram)
    return res
    
    
perm = get_permutations("assembly")
print(perm)
