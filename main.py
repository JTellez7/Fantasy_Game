import tkinter as tk
import random
import ancient_names
import weapons
import player
import combat

root = tk.Tk()

#shop and guild information
shop_money = 0
shop_inventory = []

#guild interaction
def guild():
    print(f"Greetings, {player.player_name}. What brings you to my guild?")

player.player_name = input("What is your name? ").strip().title()
guild()

root.mainloop()