import random
from fighter import Fighter

stances = ["Orthodox", "Southpaw", "Switch"]
styles = [
    "Out-Boxer", "Pressure Fighter", "Counterpuncher", 
    "Slugger", "Switch Hitter", "Boxer-Puncher", 
    "Defensive Specialist", "Brawler"
]

def generate_opponent(difficulty):
    if difficulty == "easy":
        stance = "Orthodox"
    elif difficulty == "medium":
        stance = "Southpaw"
    else:
        stance = "Switch"

    style = random.choice(styles)

    name = random.choice(["Luis 'El Toro' Ramirez", "Darnell 'Dynamite' King", "Alexis 'The Ghost' Moreno"])
    power = random.randint(6, 9)
    speed = random.randint(6, 9)
    defense = random.randint(5, 8)
    stamina = random.randint(7, 10)

    return Fighter(name, stance, style, power, speed, defense, stamina)
