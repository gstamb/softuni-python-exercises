from project.user import User
from project.movie_specification.movie import Movie
from project.movie_specification.action import Action
from project.movie_specification.thriller import Thriller
from project.movie_specification.fantasy import Fantasy
from typing import List


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def __str__(self):
        string_rep_vals = ""
        if not self.users_collection:
            string_rep_vals += "All users: No users.\n"
        else:
            string_rep_vals += f"All users: {', '.join(usr.username for usr in self.users_collection)}\n"
        if not self.movies_collection:
            string_rep_vals += "All movies: No movies.\n"
        else:
            string_rep_vals += f"All movies: {', '.join([picture.title for picture in self.movies_collection])}\n"
        return string_rep_vals.strip()

    @staticmethod
    def __fetch_obj_by_attr_val(collection, key, value):
        return next((obj for obj in collection if getattr(obj, key, None) == value), None)

    def __validate_user_is_unique(self, username: str):
        if self.__fetch_obj_by_attr_val(self.users_collection, "username", username):
            raise Exception("User already exists!")

    def __validate_upload_movie(self, username: str, movie_obj: Movie):
        target_user = self.__fetch_obj_by_attr_val(self.users_collection, "username", username)
        if not target_user:
            raise Exception("This user does not exist!")
        if movie_obj.owner != target_user:
            raise Exception(f"{username} is not the owner of the movie {movie_obj.title}!")
        if movie_obj in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        return target_user

    def __validate_edit_delete_actions_on_movie(self, username: str, movie_obj: Movie):
        target_user = self.__fetch_obj_by_attr_val(self.users_collection, "username", username)
        if movie_obj not in self.movies_collection:
            raise Exception(f"The movie {movie_obj.title} is not uploaded!")
        if movie_obj.owner != target_user:
            raise Exception(f"{username} is not the owner of the movie {movie_obj.title}!")
        return target_user

    def __validate_like_movie(self, username, movie_obj: Movie):
        target_user = self.__fetch_obj_by_attr_val(self.users_collection, "username", username)
        if movie_obj.owner == target_user:
            raise Exception(f"{username} is the owner of the movie {movie_obj.title}!")
        if movie_obj in target_user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie_obj.title}!")
        return target_user

    def __validate_dislike_movie(self, username: str, movie_obj: Movie):
        target_user = self.__fetch_obj_by_attr_val(self.users_collection, "username", username)
        if movie_obj not in target_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie_obj.title}!")
        return target_user

    def register_user(self, username: str, age: int):
        self.__validate_user_is_unique(username)
        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        target_user = self.__validate_upload_movie(username, movie)
        target_user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        self.__validate_edit_delete_actions_on_movie(username, movie)
        for key, value in kwargs.items():
            setattr(movie, key, value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        target_user = self.__validate_edit_delete_actions_on_movie(username, movie)
        self.movies_collection.remove(movie)
        target_user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        target_user = self.__validate_like_movie(username, movie)
        movie.likes += 1
        target_user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        target_user = self.__validate_dislike_movie(username, movie)
        movie.likes -= 1
        target_user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda movie: (-movie.year, movie.title))
        if sorted_movies:
            return "\n".join([movie.details() for movie in sorted_movies])
        return "No movies found."


if __name__ == "__main__":
    pass
