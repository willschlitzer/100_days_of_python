from collections import defaultdict, namedtuple, Counter, deque
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
    # Creates ordered dictionary
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            # Corrects for missing info
            except ValueError:
                continue
            # Creates named tuple with movie data
            m = Movie(title=movie, year=year, score=score)
            # Appends dictionary with movie data; director name is the key
            directors[director].append(m)
    return directors

directors = get_movies_by_director()
print(len(directors['Christopher Nolan']))

# Creates a counter object
cnt = Counter()
# Counts the movies for each director by looking at the length of the associated values for a given director
for director, movies in directors.items():
    cnt[director] += len(movies)

print(cnt.most_common(10))
