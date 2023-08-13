from project.movie import Movie
from unittest import TestCase, main


class MovieTest(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("The Matrix", 1999, 8.2)

    def test_init_valid_params(self):
        self.assertEqual("The Matrix", self.movie.name)
        self.assertEqual(1999, self.movie.year)
        self.assertEqual(8.2, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_init_invalid_name_empty(self):
        with self.assertRaises(ValueError) as err:
            Movie("", 1999, 8.2)
        error_output = "Name cannot be an empty string!"
        self.assertEqual(error_output, str(err.exception))

    def test_init_invalid_year_release(self):
        with self.assertRaises(ValueError) as err:
            Movie("First_movie_ever", 1886, 8.2)
        error_output = "Year is not valid!"
        self.assertEqual(error_output, str(err.exception))

    def test_add_actor_valid_actor_unique(self):
        actor = "Laurence Fishburne"
        self.movie.add_actor(actor)
        result = self.movie.actors
        expected = [actor]
        self.assertEqual(expected, result)

    def test_add_actor_actor_already_exists(self):
        actor = "Laurence Fishburne"
        self.movie.add_actor(actor)
        result = self.movie.add_actor(actor)
        expected = f"{actor} is already added in the list of actors!"
        self.assertEqual(expected, result)

    def test_gt_comparison_movie_ratings_movie_gt_other(self):
        other_movie = Movie("Contact", 1997, 8.1)
        result = self.movie > other_movie
        expected = f'"The Matrix" is better than "Contact"'
        self.assertEqual(expected, result)

    def test_gt_comparison_movie_ratings_other_gt_movie(self):
        other_movie = Movie("Contact", 1997, 8.3)
        result = self.movie > other_movie
        expected = f'"Contact" is better than "The Matrix"'
        self.assertEqual(expected, result)

    def test_gt_comparison_movie_ratings_other_eq_movie(self):
        other_movie = Movie("Contact", 1997, 8.2)
        result = self.movie > other_movie
        expected = f'"Contact" is better than "The Matrix"'
        self.assertEqual(expected, result)

    def test_object_representation(self):
        actor = "Keanu Reeves"
        actor1 = "Laurence Fishburne"
        self.movie.add_actor(actor)
        self.movie.add_actor(actor1)
        result = self.movie
        expected = f"Name: {self.movie.name}\n" \
                   f"Year of Release: {self.movie.year}\n" \
                   f"Rating: {self.movie.rating:.2f}\n" \
                   f"Cast: {', '.join(self.movie.actors)}"
        self.assertEqual(expected, str(result))


if __name__ == "__main__":
    pass
