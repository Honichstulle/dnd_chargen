import random

def rollstat():
    x = 0
    rolls = []

    while x < 4:
        rolls.append(random.randrange(1,7))
        x += 1 
    stat = sum(rolls) - min(rolls)
        
    return stat

def assignstats():
    stats = {
        "strength": 0,
        "dexterity": 0,
        "constitution": 0,
        "wisdom": 0,
        "intelligence": 0,
        "charisma": 0
    }

    stats['strength'] = rollstat()
    stats['dexterity'] = rollstat()
    stats['constitution'] = rollstat()
    stats['wisdom'] = rollstat()
    stats['intelligence'] = rollstat()
    stats['charisma'] = rollstat()

    print (stats)

    

assignstats()


  