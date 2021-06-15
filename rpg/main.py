import random
from classes.enemy import Enemy
from classes.game import Character, bcolors

magic = [
    {"name": "Fire", "cost": 10, "dmg": 20},
    {"name": "Thunder", "cost": 10, "dmg": 20},
    {"name": "Blizzard", "cost": 10, "dmg": 20}
]
player = Character(460, 65, 60, 34, magic)

print(player.gen_mel_dmg())
print(player.gen_mag_dmg(1))