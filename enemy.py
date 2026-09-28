import random
import weapons
import ancient_names

#enemy stats
enemy_name = ""
enemy_health = 0
enemy_shield = 0
enemy_loot = []
enemy_inventory = []

def generate_enemy():
    global enemy_name, enemy_health, enemy_shield, enemy_loot, enemy_inventory
    enemy_name = random.choice(ancient_names.npc) + " " + random.choice(ancient_names.title)
    enemy_health = random.randint(50, 100)
    enemy_shield = random.randint(0, 50)
    
    weapon_choice = random.randint(1, 3)
    if weapon_choice == 1:
        weapons.axe()
    elif weapon_choice == 2:
        weapons.sword()
    else:
        weapons.spear()
    weapons.equip_enemy_weapon()

    loot_choice = random.randint(1, 3)
    if loot_choice == 1:
        #add the weapon
        pass
    elif loot_choice == 2:
        #add gold
        pass
    else:
        #add an item
        pass