from movie_directors import get_movies_by_director
from collections import Counter
from statistics import mean


def find_highest(directors):
    """Find the highest-rated directors and print their names, scores, and films."""
    director_rating = {}
    # Counts the movies for each director by looking at the length of the associated values for a given director
    for director, movies in directors.items():
        if len(movies) >= 4:
            scores_list = []
            for movie in directors[director]:
                if movie.year >= 1960:
                    scores_list.append(movie.score)
            # Creates a dictionary with keys of the director name and their average scores
            director_rating[director] = round(mean(scores_list), 2)
    # Determines the directors with the highest average scores
    pop_directs = Counter(director_rating).most_common(5)
    for x in pop_directs:
        director = x[0]
        av_score = x[1]
        print(director + " " + str(av_score))
        print("____________________________________")
        for movie in directors[director]:
            # prints each of a director's films and the associated score
            print(movie.title + " " + str(movie.score))
        print("\n\n")


if __name__ == "__main__":
    directors = get_movies_by_director()
    find_highest(directors)
