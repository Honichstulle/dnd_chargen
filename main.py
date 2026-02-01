import random
from statroller import rollstat

def roll_class():
    class_options = ["Fighter", "Rogue", "Paladin", "Wizard", "Sorcerer", "Bard", "Druid", "Cleric", "Warlock", "Monk", "Ranger", "Barbarian"]
    return random.choice(class_options)

def roll_species():
    species_options = ["Human", "Dwarf", "Elf", "Tiefling", "Halfling", "Aasimar", "Dragonborn", "Goliath"]
    return random.choice(species_options)

def main():
    print (f"Your characer: Level 1 {roll_species()} {roll_class()}")
    print (f"Strength: {rollstat()}")
    print (f"Dexterity: {rollstat()}")
    print (f"Constitution: {rollstat()}")
    print (f"Wisdom: {rollstat()}")
    print (f"Intelligence: {rollstat()}")
    print (f"Charisma: {rollstat()}")



main()