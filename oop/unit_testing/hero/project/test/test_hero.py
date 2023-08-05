from project.hero import Hero
from unittest import TestCase, main


class HeroTest(TestCase):
    def test_initialization_params(self):
        hero = Hero("Pesho", 25, 100.0, 100.0)
        self.assertEqual("Pesho", hero.username)
        self.assertEqual(25, hero.level)
        self.assertEqual(100.0, hero.health)
        self.assertEqual(100.0, hero.damage)

    def test_battle_enemy_hero_same_usernames(self):
        hero_name = "Pesho"
        hero_level = 25
        hero_heath = 100.0
        hero_damage = 100.0
        hero = Hero(hero_name, hero_level, hero_heath, hero_damage)

        enemy_name = "Pesho"
        enemy_level = 26
        enemy_heath = 130.0
        enemy_damage = 100.0
        enemy = Hero(enemy_name, enemy_level, enemy_heath, enemy_damage)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_zero_heath_hero_battle_valid_enemy(self):
        hero_name = "Pesho"
        hero_level = 25
        hero_heath = 100.0
        hero_damage = 100.0
        hero = Hero(hero_name, hero_level, hero_heath, hero_damage)

        enemy_name = "Rambo"
        enemy_level = 26
        enemy_heath = 130.0
        enemy_damage = 100.0
        enemy = Hero(enemy_name, enemy_level, enemy_heath, enemy_damage)
        hero.health = 0
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_negative_health_hero_battle_valid_enemy(self):
        hero_name = "Pesho"
        hero_level = 25
        hero_heath = 100.0
        hero_damage = 100.0
        hero = Hero(hero_name, hero_level, hero_heath, hero_damage)

        enemy_name = "Rambo"
        enemy_level = 26
        enemy_heath = 130.0
        enemy_damage = 100.0
        enemy = Hero(enemy_name, enemy_level, enemy_heath, enemy_damage)
        hero.health = -1
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_valid_hero_battle_enemy_with_zero_heath(self):
        hero_name = "Pesho"
        hero_level = 25
        hero_heath = 100.0
        hero_damage = 100.0
        hero = Hero(hero_name, hero_level, hero_heath, hero_damage)

        enemy_name = "Rambo"
        enemy_level = 26
        enemy_heath = 130.0
        enemy_damage = 100.0
        enemy = Hero(enemy_name, enemy_level, enemy_heath, enemy_damage)

        enemy.health = 0
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)
        self.assertEqual("You cannot fight Rambo. He needs to rest", str(ex.exception))

    def test_valid_hero_battle_enemy_with_negative_heath(self):
        hero_name = "Pesho"
        hero_level = 25
        hero_heath = 100.0
        hero_damage = 100.0
        hero = Hero(hero_name, hero_level, hero_heath, hero_damage)

        enemy_name = "Rambo"
        enemy_level = 26
        enemy_heath = 130.0
        enemy_damage = 100.0
        enemy = Hero(enemy_name, enemy_level, enemy_heath, enemy_damage)

        enemy.health = -1
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)
        self.assertEqual("You cannot fight Rambo. He needs to rest", str(ex.exception))

    def test_draw_result_of_a_battle(self):
        hero_name = "Pesho"
        hero_level = 25
        hero_heath = 100.0
        hero_damage = 100.0
        hero = Hero(hero_name, hero_level, hero_heath, hero_damage)

        enemy_name = "Rambo"
        enemy_level = 26
        enemy_heath = 130.0
        enemy_damage = 100.0
        enemy = Hero(enemy_name, enemy_level, enemy_heath, enemy_damage)

        result = hero.battle(enemy)
        expected = "Draw"
        self.assertEqual(expected, result)

    def test_hero_wins_a_battle(self):
        hero_name = "Pesho"
        hero_level = 1
        hero_heath = 101.0
        hero_damage = 100.0
        hero = Hero(hero_name, hero_level, hero_heath, hero_damage)

        enemy_name = "Rambo"
        enemy_level = 1
        enemy_heath = 100.0
        enemy_damage = 100.0
        enemy = Hero(enemy_name, enemy_level, enemy_heath, enemy_damage)

        result = hero.battle(enemy)
        expected = "You win"
        self.assertEqual(expected, result)
        self.assertEqual(hero.level, 2)
        self.assertEqual(hero.health, 6)
        self.assertEqual(hero.damage, 105.0)

    def test_hero_loses_a_battle(self):
        hero_name = "Pesho"
        hero_level = 1
        hero_heath = 100.0
        hero_damage = 100.0
        hero = Hero(hero_name, hero_level, hero_heath, hero_damage)

        enemy_name = "Rambo"
        enemy_level = 1
        enemy_heath = 101.0
        enemy_damage = 100.0
        enemy = Hero(enemy_name, enemy_level, enemy_heath, enemy_damage)

        result = hero.battle(enemy)
        expected = "You lose"
        self.assertEqual(expected, result)
        self.assertEqual(enemy.level, 2)
        self.assertEqual(enemy.health, 6)
        self.assertEqual(enemy.damage, 105.0)

    def test_string_representation(self):
        hero_name = "Pesho"
        hero_level = 1
        hero_heath = 101.0
        hero_damage = 100.0
        hero = Hero(hero_name, hero_level, hero_heath, hero_damage)
        result = str(hero)

        expected = f"Hero {hero_name}: {hero_level} lvl\n" \
                   f"Health: {hero.health}\n" \
                   f"Damage: {hero.damage}\n"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
