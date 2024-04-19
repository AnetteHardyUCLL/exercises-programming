def directors(movies):
    return {movie.director for movie in movies}


def common_elements(xs, ys):
    return {common_value for common_value in xs if common_value in ys}
