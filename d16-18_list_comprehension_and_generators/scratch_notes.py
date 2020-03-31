from collections import Counter
import calendar
import itertools
import random
import re
import requests
import string


def name_loop():
    names = ["will", "john", "julie", "nick", "andrew", "ryan"]
    first_half_alphabet = list(string.ascii_lowercase)[:13]
    for name in names:
        if name[0] in first_half_alphabet:
            print(name.title())


def list_compression():
    names = ["will", "john", "julie", "nick", "andrew", "ryan"]
    first_half_alphabet = list(string.ascii_lowercase)[:13]
    print([name for name in names])
    # uses list comprehension
    print([name for name in names if name[0] in first_half_alphabet])


def get_hp():
    """Uses list comprehension on text"""
    resp = requests.get("http://projects.bobbelderbos.com/pcc/harry.txt")
    words = resp.text.lower().split()
    words = [re.sub(r"\W+", r"", word) for word in words]
    resp = requests.get("http://projects.bobbelderbos.com/pcc/stopwords.txt")
    stopwords = resp.text.lower().split()
    words = [word for word in words if word.strip() and word not in stopwords]
    cnt = Counter(words)
    print(cnt.most_common(5))


def num_gen():
    for i in range(5):
        yield i


if __name__ == "__main__":
    # name_loop()
    # list_compression()
    # get_hp()
    gen = num_gen()
    print(gen)
    print(next(gen))
    print(next(gen))
    print(next(gen))
