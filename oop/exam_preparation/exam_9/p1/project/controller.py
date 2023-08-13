from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    VALID_CATEGORY_TYPES = ["Food", "Drink"]

    def __init__(self):
        self.players = []
        self.supplies = []
        self.added_players = []

    def __str__(self):
        result_str = ""
        if self.players:
            for player in self.players:
                result_str += f"{str(player)}\n"

        if self.supplies:
            for sustenance in self.supplies:
                result_str += f"{sustenance.details()}\n"

        return result_str

    @staticmethod
    def __carry_out_duel(first_attacker, second_attacker):
        """
        Two players alternate trading blows. Damage is 50% of player's stamina.
        Player with lower stamina attacks first `first_attacker`. If the defender `second_attacker` stamina falls
        below zero, first attacker wins etc.
        If no player stamina has fallen to zero during the trading of blows. Player with higher stamina wins.
        """

        def attack(attacker, defender):
            # damage calculation
            damage = attacker.stamina / 2
            # negative stamina results in error
            defender.stamina = defender.valid_subtraction(damage)
            return defender.stamina == 0

        # First attacker strikes
        if attack(first_attacker, second_attacker):
            return f"Winner: {first_attacker.name}"

        # Second attacker strikes
        if attack(second_attacker, first_attacker):
            return f"Winner: {second_attacker.name}"

        # Determine the winner based on higher stamina
        if second_attacker.stamina > first_attacker.stamina:
            return f"Winner: {second_attacker.name}"
        return f"Winner: {first_attacker.name}"

    @staticmethod
    def __cancel_duel_if_stamina_too_low(player1, player2):
        if player1.stamina == 0 and player2.stamina == 0:
            return f"Player {player1.name} does not have enough stamina.\n" \
                   f"Player {player2.name} does not have enough stamina."
        else:
            if player1.stamina == 0:
                return f"Player {player1.name} does not have enough stamina."
            if player2.stamina == 0:
                return f"Player {player2.name} does not have enough stamina."

    def __validate_sustain(self, requested_sustenance):
        """ Raises an exception if no sustenance items of the desired category are left """
        for sustenance_category in self.VALID_CATEGORY_TYPES:
            if requested_sustenance == sustenance_category:
                category_items_left = [item for item in self.supplies if item.__class__.__name__ == sustenance_category]
                if not category_items_left:
                    raise Exception(f"There are no {sustenance_category.lower()} supplies left!")

    def add_player(self, *args: Player):
        added_player_names = []
        [(added_player_names.append(new_player.name), self.players.append(new_player))
         for new_player in args
         if new_player not in self.players]
        if added_player_names:
            self.added_players.extend(added_player_names)
        return f"Successfully added: {', '.join(added_player_names)}"

    def add_supply(self, *args: Supply):
        [self.supplies.append(supply) for supply in args]

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in self.VALID_CATEGORY_TYPES or player_name not in self.added_players:
            return
        player = next((obj for obj in self.players if getattr(obj, "name", None) == player_name), None)
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        self.__validate_sustain(sustenance_type)

        for index in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[index].__class__.__name__ == sustenance_type:
                sustenance_product = self.supplies.pop(index)
                if player.stamina + sustenance_product.energy > 100:
                    player.stamina = 100
                else:
                    player.stamina += sustenance_product.energy
                return f"{player_name} sustained successfully with {sustenance_product.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = next((obj for obj in self.players if getattr(obj, "name", None) == first_player_name), None)
        player2 = next((obj for obj in self.players if getattr(obj, "name", None) == second_player_name), None)

        should_cancel_duel = self.__cancel_duel_if_stamina_too_low(player1, player2)
        if should_cancel_duel:
            return should_cancel_duel

        order_of_attackers = sorted([player1, player2], key=lambda player: -player.stamina)
        first_attacker = order_of_attackers.pop()
        second_attacker = order_of_attackers.pop()

        return self.__carry_out_duel(first_attacker, second_attacker)

    def next_day(self):
        if self.players:
            for player in self.players:
                player.stamina = player.valid_subtraction(player.age * 2)
                self.sustain(player.name, "Food")
                self.sustain(player.name, "Drink")
        else:
            return "All players have left!"


if __name__ == "__main__":
    pass
