import random
import ancient_names

#current weapon stats
weapon_name = ""
weapon_damage = 0
weapon_durability = 0
armor_piercing = False

#new weapon stats
new_weapon_name = ""
new_weapon_damage = 0
new_weapon_durability = 0
new_armor_piercing = False

#weapons
def axe():
    global new_weapon_name, new_weapon_damage, new_weapon_durability, new_armor_piercing
    new_weapon_name = "Axe of " + random.choice(ancient_names.weapon_names)
    new_weapon_damage = random.randint(15, 25)
    new_weapon_durability = random.randint(10, 15)
    new_armor_piercing = False

def sword():
    global new_weapon_name, new_weapon_damage, new_weapon_durability, new_armor_piercing
    new_weapon_name = "Sword of " + random.choice(ancient_names.weapon_names)
    new_weapon_damage = random.randint(10, 20)
    new_weapon_durability = random.randint(15, 20)
    new_armor_piercing = False

def spear():
    global new_weapon_name, new_weapon_damage, new_weapon_durability, new_armor_piercing
    new_weapon_name = "Spear of " + random.choice(ancient_names.weapon_names)
    new_weapon_damage = random.randint(5, 15)
    new_weapon_durability = random.randint(5, 10)
    new_armor_piercing = True

#equip the new weapon
def equip_weapon():
    global weapon_name, weapon_damage, weapon_durability, armor_piercing
    weapon_name = new_weapon_name
    weapon_damage = new_weapon_damage
    weapon_durability = new_weapon_durability
    armor_piercing = new_armor_piercing
    print(f"You have equipped the {weapon_name}.")

#enemy weapon
def equip_enemy_weapon():
    global enemy_weapon_name, enemy_weapon_damage, enemy_weapon_durability, enemy_armor_piercing
    enemy_weapon_name = new_weapon_name
    enemy_weapon_damage = new_weapon_damage
    enemy_weapon_durability = new_weapon_durability
    enemy_armor_piercing = new_armor_piercing