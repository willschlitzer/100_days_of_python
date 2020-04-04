from itertools import permutations

wordfile = "words_alpha.txt"

with open(wordfile, "r") as f:
    wordlist = f.read().splitlines()


def find_anagrams(word, wordlist=wordlist):
    word_perms = list(permutations(word))
    print(len(word_perms))
    anagram_list = []
    for perm in word_perms:
        perm_word = "".join(perm).lower()
        if (
            (perm_word in wordlist)
            and (perm_word not in anagram_list)
            and (perm_word != word)
        ):
            anagram_list.append(perm_word)
    print(anagram_list)


word = "a"
find_anagrams(word=word)
