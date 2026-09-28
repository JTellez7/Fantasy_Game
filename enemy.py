import random
import weapons
import ancient_names

#create an enemy
class Enemy:
    def __init__(self, name, health, shield, loot, inventory, en_weapon):
        self.name = name
        self.health = health
        self.shield = shield
        self.loot = loot
        self.inventory = inventory
        self.en_weapon = en_weapon

def generate_enemy(Enemy):
    return Enemy(
        name=random.choice(ancient_names.npc) + " " + random.choice(ancient_names.title),
        health=random.randint(50, 100),
        shield=random.randint(0, 50),
        loot=random.choice(["gold", "item", "weapon"]),
        inventory=[],
        en_weapon=random.choice([weapons.axe(), weapons.sword(), weapons.spear()])
    )


enemy = generate_enemy(Enemy)

print(f"Name: {enemy.name}, Health: {enemy.health}, Shield: {enemy.shield}, Loot: {enemy.loot}, Inventory: {enemy.inventory}, Enemy Weapon: {enemy.en_weapon}")