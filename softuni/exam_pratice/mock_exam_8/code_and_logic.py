class Hero:
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana

    def cast_spell(self, mana_needed, spell_name):
        if self.mana >= mana_needed:
            self.mana -= mana_needed
            print(f"{self.name} has successfully cast {spell_name} and now has {self.mana} MP!")
        else:
            print(f"{self.name} does not have enough MP to cast {spell_name}!")

    def take_damage(self, dmg, attacker):
        if self.hp - dmg > 0:
            self.hp -= dmg
            print(f"{self.name} was hit for {dmg} HP by {attacker} and now has {self.hp} HP left!")
        else:
            self.hp -= dmg
            print(f"{self.name} has been killed by {attacker}!")

    def recharge(self, amount):
        start = self.mana
        if self.mana + amount > 200:
            self.mana = 200
        else:
            self.mana += amount
        print(f"{self.name} recharged for {self.mana - start} MP!")

    def heal(self, amount):
        start = self.hp
        if self.hp + amount > 100:
            self.hp = 100
        else:
            self.hp += amount
        print(f"{self.name} healed for {self.hp - start} HP!")

    def __repr__(self):
        return f"{self.name}-{self.hp}-{self.mana}"


heroes = {}
for i in range(int(input())):
    name, hp, mana = input().split()
    hero = Hero(name, int(hp), int(mana))
    heroes[name] = hero
while True:

    instruction = input()
    if instruction == "End":
        break

    if instruction.startswith("Heal"):
        _, hero, amount = instruction.split(" - ")
        heroes[hero].heal(int(amount))
    elif instruction.startswith("TakeDamage"):
        _, hero, damage, enemy = instruction.split(" - ")
        heroes[hero].take_damage(dmg=int(damage), attacker=enemy)
    elif instruction.startswith("Recharge"):
        _, hero, amount = instruction.split(" - ")
        heroes[hero].recharge(amount=int(amount))
    elif instruction.startswith("Cast"):
        _, hero, mana, spell_name = instruction.split(" - ")
        heroes[hero].cast_spell(int(mana), spell_name)

for hero in heroes:
    if heroes[hero].hp > 0:
        print(hero)
        print(f" HP: {heroes[hero].hp}")
        print(f" MP: {heroes[hero].mana}")
