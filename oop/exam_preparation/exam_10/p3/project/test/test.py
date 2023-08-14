from project.team import Team
from unittest import TestCase, main
from typing import Dict


class TeamTest(TestCase):
    def setUp(self) -> None:
        self.team = Team("AFU")

    def test_init_valid_params(self):
        self.assertEqual("AFU", self.team.name)
        self.assertEqual(dict(), self.team.members)

    def test_init_invalid_name(self):
        with self.assertRaises(ValueError) as err:
            Team("Asd123")
        self.assertEqual("Team Name can contain only letters!", str(err.exception))

    def test_team_add_members(self):
        self.team.add_member(Zoltan=22)
        members = ["Zlatan", "Piotyr", "Oleksandyr"]
        result = self.team.add_member(Zlatan=45, Piotyr=22, Oleksandyr=37)
        expected = f"Successfully added: {', '.join(members)}"
        self.assertEqual(expected, result)
        self.assertEqual({"Zoltan": 22, "Zlatan": 45, "Piotyr": 22, "Oleksandyr": 37}, self.team.members)

    def test_remove_members_target_memeber_exists(self):
        members = ["Zlatan", "Piotyr", "Oleksandyr"]
        self.team.add_member(Zlatan=45, Piotyr=22, Oleksandyr=37)
        member_to_remove = "Zlatan"
        result = self.team.remove_member(member_to_remove)
        expected = f"Member {member_to_remove} removed"
        self.assertEqual(expected, result)
        self.assertEqual({"Piotyr": 22, "Oleksandyr": 37}, self.team.members)

    def test_remove_members_target_memeber_does_not_exist(self):
        members = ["Zlatan", "Piotyr", "Oleksandyr"]
        self.team.add_member(Zlatan=45, Piotyr=22, Oleksandyr=37)
        member_to_remove = "Alex"
        result = self.team.remove_member(member_to_remove)
        expected = f"Member with name {member_to_remove} does not exist"
        self.assertEqual(expected, result)

    def test_compare_two_team_instances(self):
        other = Team("BGR")
        members = ["Zlatan", "Piotyr", "Oleksandyr"]
        other.add_member(Zlatan=45, Piotyr=22, Oleksandyr=37)
        result = self.team > other
        expected = False
        self.assertEqual(expected, result)

    def test_compare_two_teams_equal_length(self):
        other = Team("BGR")
        self.team.add_member(Zlatan=12)
        other.add_member(Peter=13)
        result = self.team > other
        expected = False
        self.assertEqual(expected, result)

    def test_compare_two_teams_first_team_bigger(self):
        other = Team("BGR")
        self.team.add_member(Zlatan=12)
        result = self.team > other
        expected = True
        self.assertEqual(expected, result)

    def test_len_function(self):
        self.team.add_member(Zlatan=45, Piotyr=22, Oleksandyr=37)
        result = len(self.team)
        expected = 3
        self.assertEqual(expected, result)

    def test_add_function(self):
        other = Team("BGR")
        self.team.add_member(Zlatan=12)
        other.add_member(Peter=13)
        result = self.team + other
        self.assertIsInstance(result, Team)
        self.assertEqual("AFUBGR", result.name)
        self.assertEqual({"Zlatan": 12, "Peter": 13}, result.members)

    def test_string_representation_str(self):
        self.team.add_member(Zlatan=45, Piotyr=22, Oleksandyr=37)
        result = str(self.team)
        expected = "Team name: AFU\nMember: Zlatan - 45-years old\nMember: Oleksandyr - 37-years old\nMember: Piotyr - 22-years old"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
