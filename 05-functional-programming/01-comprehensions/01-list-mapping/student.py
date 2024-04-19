def titles(movies):
    return [movie.title for movie in movies]


def titles_and_years(movies):
    return [(movie.title, movie.year) for movie in movies]


def titles_and_actor_counts(movies):
    return [(movie.title, len(movie.actors)) for movie in movies]


def reverse_words(sentence):
    return " ".join([word[::-1] for word in sentence.split(" ")])
