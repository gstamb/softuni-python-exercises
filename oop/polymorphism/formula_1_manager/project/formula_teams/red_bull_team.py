from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    SPONSOR_1 = {
        1: 1500000,
        2: 800000,
    }

    SPONSOR_2 = {
        8: 20000,
        10: 10000
    }
    EXPENSES = 250000

    def __init__(self, budget):
        super().__init__(budget)
        if budget < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.budget = budget
        self.__class__.budget = budget


