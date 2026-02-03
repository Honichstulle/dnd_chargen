class PlayerSpecies:
    def __init__(self):
        self.name = "name"

    def return_name(self):
        return self.name

class Human(PlayerSpecies):
    def __init__(self):
        self.name = "Human"

class Dwarf(PlayerSpecies):
    def __init__(self):
        self.name = "Dwarf"

class Elf(PlayerSpecies):
    def __init__(self):
        self.name = "Elf"

class Halfling(PlayerSpecies):
    def __init__(self):
        self.name = "Halfling"

class Gnome(PlayerSpecies):
    def __init__(self):
        self.name = "Gnome"

class Tiefling(PlayerSpecies):
    def __init__(self):
        self.name = "Tiefling"

class Aasimar(PlayerSpecies):
    def __init__(self):
        self.name = "Aasimar"

class Goliath(PlayerSpecies):
    def __init__(self):
        self.name = "Goliath"
