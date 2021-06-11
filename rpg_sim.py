import random

class Enemy:
    health = 200

    def __init__(self, atk_low, atk_hi):
        self.atk_low = atk_low
        self.atk_hi = atk_hi


    def get_atk_low(self):
        print(self.atk_low)

    def get_health(self):
        print("Total Health:", self.health)

class Player:
    def __init__(self, health):
        self.health = health


troll = Enemy(50, 70)

goblin = Enemy(40, 80)

player = Player(500)


while player.health > 0:
    dmg = random.randrange(troll.atk_low, troll.atk_hi)
    player_hp = player.health - dmg


    print("Enemy strikes for", dmg, "points of damage. Current HP is", player_hp)

    if player_hp <= 0:
        player_hp = 0

    if player_hp == 0:
        print("You have died.")
        break

    if player_hp <= 30:
        print("Your health is at", player_hp, ". You escape with your life")
        break
    