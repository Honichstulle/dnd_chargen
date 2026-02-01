import random
import inspect
from statroller import rollstat, assignstats
from classes import *

class_options = [Fighter, Barbarian, Warlock, Wizard, Sorcerer, Bard, Druid, Cleric, Paladin, Monk, Rogue, Ranger]
# Create random class instance
player_class = random.choice(class_options)()
primary_stat = player_class.return_primary()
player_stats = assignstats(primary_stat)


def roll_species():
    species_options = ["Human", "Dwarf", "Elf", "Tiefling", "Halfling", "Aasimar", "Dragonborn", "Goliath"]
    return random.choice(species_options)
    

def main():
    print (f"Your characer: Level 1 {roll_species()} {player_class.return_name()}")
    print (f"Strength: {player_stats['strength']}")
    print (f"Dexterity: {player_stats['dexterity']}")
    print (f"Constitution: {player_stats['constitution']}")
    print (f"Wisdom: {player_stats['wisdom']}")
    print (f"Intelligence: {player_stats['intelligence']}")
    print (f"Charisma: {player_stats['charisma']}")



main()