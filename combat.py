import random
import player
import enemy
import weapons

combat_active = False

#Start combat
def start_combat():
    global combat_active
    enemy.enemy = enemy.generate_enemy(enemy.Enemy)
    combat_active = True
    
#combat function
def player_attack():
    global combat_active
    #calculate the damage
    
    #damage the enemy
    if weapons.armor_piercing:
        enemy.enemy.health -= weapons.weapon_damage
    elif enemy.enemy.shield > 0:
        if weapons.weapon_damage <= enemy.enemy.shield:
            enemy.enemy.shield -= weapons.weapon_damage
        else:
            remaining_damage = weapons.weapon_damage - enemy.enemy.shield
            enemy.enemy.shield = 0
            enemy.enemy.health -= remaining_damage
    else:
        enemy.enemy.health -= weapons.weapon_damage

    #calculate weapon durability
    weapons.weapon_durability -= 1
    weapons.check_durability()

    #check if the enemy is dead
    if enemy.enemy.health <= 0:
        print(f"{enemy.enemy.name} has been slain.")
        combat_active = False
    else:
        enemy_attack()

def use_item(item):
    #consume the item and apply its effects
    pass

def run_away():
    #attempt to escape from combat
    pass

def enemy_attack():
    global combat_active
    #calculate the damage
    
    #damage the player
    if weapons.enemy_weapon.armor_piercing:
        player.player_health -= weapons.enemy_weapon.damage
    elif player.player_shield > 0:
        if weapons.enemy_weapon.damage <= player.player_shield:
            player.player_shield -= weapons.enemy_weapon.damage
        else:
            remaining_damage = weapons.enemy_weapon.damage - player.player_shield
            player.player_shield = 0
            player.player_health -= remaining_damage
    else:
        player.player_health -= weapons.enemy_weapon.damage
    #check if the player is dead
    if player.player_health <= 0:
        print(f"You have been slain.")
        combat_active = False

start_combat()
player_attack()
player_attack()