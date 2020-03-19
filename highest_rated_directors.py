from movie_directors import Movie, movie_data, movies_csv, get_movies_by_director
from collections import defaultdict, namedtuple, Counter, deque
import csv
# import random
from urllib.request import urlretrieve
from statistics import mean


urlretrieve(movie_data, movies_csv)

def find_highest(directors):
    cnt = Counter()
    director_rating = defaultdict(list)
    # Counts the movies for each director by looking at the length of the associated values for a given director
    for director, movies in directors.items():
        if len(movies) >= 4:
            scores_list = []
            for movie in directors[director]:
                scores_list.append(movie.score)
            director_rating[director] = mean(scores_list)
    print(Counter(director_rating).most_common(10))

if __name__ == "__main__":
    directors = get_movies_by_director()
    find_highest(directors)
    #print(directors)

