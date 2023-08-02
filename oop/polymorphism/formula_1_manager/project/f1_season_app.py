from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    red_bull_team = None
    mercedes_team = None

    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team, budget):
        if team == "Red Bull":
            new_team = RedBullTeam(budget)
            self.red_bull_team = new_team
            self.__class__.red_bull_team = new_team
            return f"{team} has joined the new F1 season."
        elif team == "Mercedes":
            new_team = MercedesTeam(budget)
            self.mercedes_team = new_team
            self.__class__.mercedes_team = new_team
            return f"{team} has joined the new F1 season."
        else:
            raise ValueError("Invalid team name!")

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if self.mercedes_team is None or self.red_bull_team is None:
            raise Exception("Not all teams have registered for the season.")
        else:
            mercedes_revenue = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)
            red_bull_revenue = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
            ahead = ["Red Bull" if red_bull_revenue > mercedes_revenue else "Mercedes"]
            return f"Red Bull: {red_bull_revenue}. Mercedes: {mercedes_revenue}. {ahead[0]} is ahead at the {race_name} race."
