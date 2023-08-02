from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    SPONSOR_1 = {
        1: 1000000,
        2: 500000}

    SPONSOR_2 = {
        5: 100000,
        7: 50000
    }
    EXPENSES = 200000

    def __init__(self, budget):
        super().__init__(budget)
