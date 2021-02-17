from classes.game import Person, bcolors

magic = [
    {"name": "Fire", "cost": 10, "dmg": 60},
    {"name": "Thunder", "cost": 15, "dmg": 80},
    {"name": "Blizzard", "cost": 40, "dmg": 160},
]

player = Person(500, 70, 50, 34, magic)

print(player.generate_damage())
print(player.generate_spell_damage())
