from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    SPONSOR_1 = {}
    SPONSOR_2 = {}
    EXPENSES = 0
    budget = 0

    @abstractmethod
    def __init__(self, budget: int):
        self.budget = budget
        self.__class__.budget = budget

    @property
    def budget(cls):
        return cls._budget

    @budget.setter
    def budget(cls, budget):
        if budget < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        else:
            cls._budget = budget

    def calculate_revenue_after_race(self, race_pos: int):
        race_revenue = self.calculate_revenue_sponsor_1(race_pos) + self.calculate_revenue_sponsor_2(race_pos)
        expenses = getattr(self.__class__, "EXPENSES")
        gross_profit = race_revenue - expenses
        self.budget += gross_profit
        self.__class__.budget += gross_profit
        return f"The revenue after the race is {gross_profit}$. Current budget {self.budget}$"

    @classmethod
    def calculate_revenue_sponsor_1(cls, final_position: int):
        paid_positions_sponsor_1 = getattr(cls, "SPONSOR_1")
        race_revenue = 0
        if final_position in paid_positions_sponsor_1:
            race_revenue += paid_positions_sponsor_1[final_position]

        return race_revenue

    @classmethod
    def calculate_revenue_sponsor_2(cls, final_position: int):
        paid_positions_sponsor_2 = getattr(cls, "SPONSOR_2")
        min_paid_pos_sponsor_2 = min(paid_positions_sponsor_2.keys())
        race_revenue = 0
        if final_position in paid_positions_sponsor_2:
            race_revenue += paid_positions_sponsor_2[final_position]
        else:
            if final_position < min_paid_pos_sponsor_2:
                paid_pos = min_paid_pos_sponsor_2
                race_revenue += cls.SPONSOR_2[paid_pos]

        return race_revenue
