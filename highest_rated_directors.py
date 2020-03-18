from movie_directors import Movie, movie_data, movies_csv, get_movies_by_director
from collections import defaultdict, namedtuple, Counter, deque
import csv
# import random
from urllib.request import urlretrieve

urlretrieve(movie_data, movies_csv)

def find_highest(directors):
    cnt = Counter()
    # Counts the movies for each director by looking at the length of the associated values for a given director
    for director, movies in directors.items():
        if len(movies) >= 4:
            print(directors[director][2])

if __name__ == "__main__":
    directors = get_movies_by_director()
    find_highest(directors)
    #print(directors)

