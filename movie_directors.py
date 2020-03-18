# from collections import defaultdict, namedtuple, Counter, deque
import csv

# import random
from urllib.request import urlretrieve

# Retrieves movie data from source; saves as CSV
movie_data = "https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv"
movies_csv = "movies.csv"
urlretrieve(movie_data, movies_csv)

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director(data=movies_csv):
    "Extracts the movies from the CSV file and stores them in a dictionary"
    directors = defaultdict(list)
