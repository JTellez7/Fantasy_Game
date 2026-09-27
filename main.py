import tkinter as tk
import random
import ancient_names
import weapons
import player

root = tk.Tk()

#enemy stats
enemy_loot = []
enemy_health = 0
enemy_shield = 0
enemy_inventory = []

#shop and guild information
shop_money = 0
shop_inventory = []


#combat function
def combat():
    global player.player_health, player.player_shield, enemy_health, enemy_shield
    if player.player_health <= 0 or enemy_health <= 0:
        print("Combat has ended.")

#guild interaction
def guild():
    print(f"Greetings, {player.player_name}. What brings you to my guild?")

player.player_name = input("What is your name? ").strip().title()
guild()

root.mainloop()