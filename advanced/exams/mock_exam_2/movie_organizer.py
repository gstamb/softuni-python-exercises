def movie_organizer(*args):
    """ Groups movie by genre from a variable number of tuple arguments containing movie name and genre.
        Return a string containing a list of movies and total count for each genre.
        Genre - [count_movies]
        * [movie_name_1]
        * [movie_name_2]
        ...
    """
    movie_genre = {}
    for movie, genre in args:
        if genre not in movie_genre:
            movie_genre[genre] = [movie]
        else:
            movie_genre[genre].append(movie)
    movies_list = ""
    for genre, movies in sorted(movie_genre.items(), key=lambda x: (-len(x[1]), x[0])):
        movies_list += f"{genre} - {len(movies)}\n"
        movies_list += "* {0}\n".format('\n* '.join(sorted(movies)))
    return movies_list


def main():
    print(movie_organizer(
        ("The Godfather", "Drama"),
        ("The Hangover", "Comedy"),
        ("The Shawshank Redemption", "Drama"),
        ("The Pursuit of Happiness", "Drama"),
        ("The Hangover Part II", "Comedy")))


if __name__ == "__main__":
    main()
