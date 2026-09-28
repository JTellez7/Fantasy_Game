import random
import ancient_names

#create a weapon
class Weapon:
    def __init__(self, name, damage, durability, armor_piercing):
        self.name = name
        self.damage = damage
        self.durability = durability
        self.armor_piercing = armor_piercing
    #check the durability of the weapon
    def check_durability(self):
        if self.durability <= 0:
            print(f"The {self.name} has broken.")
            self.damage = self.damage // 2
#weapons
def axe():
    return Weapon("Axe of " + random.choice(ancient_names.weapon_names)
    , random.randint(15, 25), random.randint(10, 15), False)

def sword():
    return Weapon("Sword of " + random.choice(ancient_names.weapon_names)
    , random.randint(10, 20), random.randint(15, 20), False)

def spear():
    return Weapon("Spear of " + random.choice(ancient_names.weapon_names)
    , random.randint(5, 15), random.randint(5, 10), True)
