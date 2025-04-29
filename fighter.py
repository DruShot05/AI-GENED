class Fighter:
    def __init__(self, name, stance, style, power, speed, defense, stamina):
        self.name = name
        self.stance = stance
        self.style = style
        self.power = power
        self.speed = speed
        self.defense = defense
        self.stamina = stamina
        self.health = 100  # Default

    def display(self):
        print(f"{self.name} - {self.stance} Stance - {self.style}")
        print(f"Stats -> Power: {self.power}, Speed: {self.speed}, Defense: {self.defense}, Stamina: {self.stamina}")
