class Playerclass:
    def __init__(self):
        self.name = "name"
        self.primary = "primary"
    
    def return_name(self):
        return self.name
    
    def return_primary(self):
        return self.primary
    

class Fighter(Playerclass):
    def __init__(self):
        self.name = "Fighter"
        self.primary = "strength"

class Rogue(Playerclass):
    def __init__(self):
        self.name = "Rogue"
        self.primary = "dexterity"

class Wizard(Playerclass):
    def __init__(self):
        self.name = "Wizard"
        self.primary = "intelligence"

class Druid(Playerclass):
    def __init__(self):
        self.name = "Druid"
        self.primary = "wisdom"

class Warlock(Playerclass):
    def __init__(self):
        self.name = "Warlock"
        self.primary = "charisma"

class Sorcerer(Playerclass):
    def __init__(self):
        self.name = "Sorcerer"
        self.primary = "charisma"

class Bard(Playerclass):
    def __init__(self):
        self.name = "Bard"
        self.primary = "charisma"

class Barbarian(Playerclass):
    def __init__(self):
        self.name = "Barbarian"
        self.primary = "strength"

class Cleric(Playerclass):
    def __init__(self):
        self.name = "Cleric"
        self.primary = "wisdom"

class Paladin(Playerclass):
    def __init__(self):
        self.name = "Paladin"
        self.primary = "strength"

class Monk(Playerclass):
    def __init__(self):
        self.name = "Monk"
        self.primary = "dexterity"

class Ranger(Playerclass):
    def __init__(self):
        self.name = "Ranger"
        self.primary = "dexterity"

