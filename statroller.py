import random

def rollstat():
    x = 0
    rolls = []

    # Roll a D6 four times, drop the lowest number rolled
    while x < 4:
        rolls.append(random.randrange(1,7))
        x += 1 
    stat = sum(rolls) - min(rolls)
        
    return stat

def assignstats(primary):

    char_stats = []
    stats = {
        "strength": 0,
        "dexterity": 0,
        "constitution": 0,
        "wisdom": 0,
        "intelligence": 0,
        "charisma": 0
    }

    x = 0

    # Roll 6 times for the six stats
    while x < 6:
        char_stats.append(rollstat())
        x += 1

    # Use the highest value for the characters primary stat, then remove it from the list
    stats[primary] = max(char_stats)
    char_stats.remove(max(char_stats))

    # Assign the remaining values to the characters other stats
    for stat in stats:
        if stat == primary:
            continue
        pick = random.choice(char_stats)
        stats[stat] = pick
        char_stats.remove(pick)

    return stats




  