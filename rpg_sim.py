import random

player_hp = 340
enemy_atk_low = 60
enemy_atk_hi = 80

while player_hp > 0:
    dmg = random.randrange(enemy_atk_low, enemy_atk_hi)
    player_hp = player_hp - dmg


    print("Enemy strikes for", dmg, "points of damage. Current HP is", player_hp)

    if player_hp <= 0:
        player_hp = 0

    if player_hp == 0:
        print("You have died.")
        break

    if player_hp <= 30:
        print("Your health is at", player_hp, ". You escape with your life")
        break
    

