import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

    # Create dynamic dice options
diceOptions = list(range(1, 7))  # [1, 2, 3, 4, 5, 6]

def main():
    # Available weapons
    weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

    # Display weapons
    print("\nAvailable Weapons:")
    for i, weapon in enumerate(weapons, start=1):
        print(f"{i}. {weapon}")

    # Input validation for combat strength
    while True:
        try:
            combatStrength = int(input("Enter your combat strength (1-6): "))
            if 1 <= combatStrength <= 6:
                break
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            mCombatStrength = int(input("Enter the monster's combat strength (1-6): "))
            if 1 <= mCombatStrength <= 6:
                break
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter an integer.")



    # Start battle simulation
    print("\nStarting the battle simulation!")
    for round_num in range(1, 20, 2):  # Simulate rounds 1, 3, 5, ..., 19
        hero_roll = random.choice(diceOptions)
        monster_roll = random.choice(diceOptions)

        # Add dice rolls to combat strengths
        hero_strength = combatStrength + hero_roll
        monster_strength = mCombatStrength + monster_roll

        # Select weapons based on dice rolls
        hero_weapon = weapons[hero_roll - 1]
        monster_weapon = weapons[monster_roll - 1]

        # Announce the round details
        print(f"\nRound {round_num}: Hero rolled {hero_roll}, Monster rolled {monster_roll}.")
        print(f"Hero selected: {hero_weapon}, Monster selected: {monster_weapon}.")
        print(f"Hero Total Strength: {hero_strength}, Monster Total Strength: {monster_strength}.")

        # Determine the winner
        if hero_strength > monster_strength:
            print("Hero wins the round!")
        elif hero_strength < monster_strength:
            print("Monster wins the round!")
        else:
            print("It's a tie!")

        # Check for the break condition
        if round_num == 11:
            print("\nBattle Truce declared in Round 11. Game Over!")
            break

if __name__ == "__main__":
    main()
