import random
import inspect
from statroller import rollstat, assignstats
from classes import *
from species import *

class_options = [Fighter, Barbarian, Warlock, Wizard, Sorcerer, Bard, Druid, Cleric, Paladin, Monk, Rogue, Ranger]
# Create random class instance -> Class
player_class = random.choice(class_options)()
primary_stat = player_class.return_primary()
player_stats = assignstats(primary_stat)

species_options = [Human, Dwarf, Elf, Halfling, Gnome, Tiefling, Aasimar, Goliath]
# Create random class instance -> Species
player_species = random.choice(species_options)()
    

def main():
    with open("character.txt","w") as f:
        print (f"Your characer: Level 1 {player_species.return_name()} {player_class.return_name()}", file=f)
        print (f"Strength: {player_stats['strength']}", file=f)
        print (f"Dexterity: {player_stats['dexterity']}", file=f)
        print (f"Constitution: {player_stats['constitution']}", file=f)
        print (f"Wisdom: {player_stats['wisdom']}", file=f)
        print (f"Intelligence: {player_stats['intelligence']}", file=f)
        print (f"Charisma: {player_stats['charisma']}", file=f)



main()