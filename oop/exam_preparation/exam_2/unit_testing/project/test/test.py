# from project.tennis_player import TennisPlayer
from unit_testing.project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("gogo", 30, 1000)

    def test_initialization_valid_params(self):
        self.assertEqual(self.player.name, "gogo")
        self.assertEqual(self.player.age, 30)
        self.assertEqual(self.player.points, 1000)
        self.assertEqual(self.player.wins, [])

    def test_too_short_player_name(self):
        with self.assertRaises(ValueError) as ex:
            TennisPlayer("gg", 30, 100)
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_too_short_player_name_no_name(self):
        with self.assertRaises(ValueError) as ex:
            TennisPlayer("", 30, 100)
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_change_name_too_short_player_name(self):
        player = TennisPlayer("gogo", 30, 100)
        with self.assertRaises(ValueError) as ex:
            player.name = ""
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_change_name_too_short_player_name_min_length(self):
        player = TennisPlayer("gogo", 30, 100)
        with self.assertRaises(ValueError) as ex:
            player.name = "gg"
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_player_age_player_too_young(self):
        with self.assertRaises(ValueError) as ex:
            TennisPlayer("gogo", 17, 100)
        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test_change_age_below_minimum_age(self):
        player = TennisPlayer("gogo", 30, 100)
        with self.assertRaises(ValueError) as ex:
            player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test_adding_new_win_already_recorded(self):
        tournament_name = "Tournament#1"
        self.player.wins.append(tournament_name)
        result = self.player.add_new_win(tournament_name)
        expected = "Tournament#1 has been already added to the list of wins!"
        self.assertEqual(expected, result)

    def test_adding_new_win_not_recorded(self):
        tournament_name = "Tournament#1"
        self.player.add_new_win(tournament_name)
        result = tournament_name in self.player.wins
        expected = True
        self.assertEqual(expected, result)

    def test_comparing_players_by_points_lt(self):
        player2 = TennisPlayer("Pesho", 19, 2000)
        result = TennisPlayer.__lt__(self.player, player2)
        expected = f'{player2.name} is a top seeded player and he/she is better than {self.player.name}'
        self.assertEqual(expected, result)

    def test_comparing_players_by_points_lt_reversed(self):
        player2 = TennisPlayer("Pesho", 19, 500)
        result = TennisPlayer.__lt__(self.player, player2)
        expected = f'{self.player.name} is a better player than {player2.name}'
        self.assertEqual(expected, result)

    def test_str_representation_no_wins(self):
        result = str(self.player)
        expected = f"Tennis Player: gogo\n" \
                   f"Age: 30\n" \
                   f"Points: 1000.0\n" \
                   f"Tournaments won: "
        self.assertEqual(expected, result)

    def test_str_representation_with_wins(self):
        self.player.add_new_win("Tournament#1")
        self.player.add_new_win("Tournament#2")
        result = str(self.player)
        expected = f"Tennis Player: gogo\n" \
                   f"Age: 30\n" \
                   f"Points: 1000.0\n" \
                   f"Tournaments won: Tournament#1, Tournament#2"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
