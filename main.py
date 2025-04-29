from fighter import Fighter
from opponent import generate_opponent
from utils import select_move
from moves import move_effects

def create_player():
    name = input("Enter your fighter's name: ")
    stance = input("Choose your stance (Orthodox/Southpaw/Switch): ")
    style = input("Choose your style (Out-Boxer/Pressure Fighter/Counterpuncher/etc): ")

    # You can later make these choices too
    power = int(input("Assign power (1-10): "))
    speed = int(input("Assign speed (1-10): "))
    defense = int(input("Assign defense (1-10): "))
    stamina = int(input("Assign stamina (1-10): "))

    return Fighter(name, stance, style, power, speed, defense, stamina)

def fight(player, opponent):
    round_number = 1
    while player.health > 0 and opponent.health > 0:
        print(f"\n--- Round {round_number} ---")
        for _ in range(5):  # 5 actions = 1 round
            move = select_move()
            effect = move_effects[move]

            player.stamina -= effect["stamina_cost"]
            opponent.health -= effect["damage"]

            print(f"You used {move}! Opponent health is now {opponent.health}")

            if opponent.health <= 0:
                break

        if opponent.health > 0:
            opponent_damage = 5
            player.health -= opponent_damage
            print(f"Opponent hits back! Your health is now {player.health}")

        round_number += 1

    if player.health > 0:
        print("\n🏆 You win the fight!")
    else:
        print("\n❌ You lost the fight...")

def main():
    print("Welcome to the Boxing Simulator!")

    difficulty = input("Choose opponent difficulty (easy/medium/hard): ")
    opponent = generate_opponent(difficulty)

    print("\nYour opponent is:")
    opponent.display()

    player = create_player()

    fight(player, opponent)

if __name__ == "__main__":
    main()
