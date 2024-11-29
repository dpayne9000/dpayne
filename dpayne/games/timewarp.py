import random
import time


def main():
    # ASCII Art for characters
    player_art = """
    O
    /|\\
    / \\
    """

    office_worker_art = """
        O
    /|\\
    /|||\\
    | |
    /   \\
    """

    # Battle setup
    player_health = 100
    office_worker_health = 150
    player_attack_range = (10, 20)
    office_worker_attack_range = (15, 25)

    inventory = {
        "Potion": 3,  # Restores health
        "Coffee": 2,  # Boosts attack power temporarily
        "Stapler": 1,  # Can be thrown at the office worker
    }

    # Spell setup
    spells = {
        "Fireball": {"damage": (15, 25), "cost": 10},
        "Ice Blast": {"damage": (10, 20), "cost": 5, "effect": "freeze"},
        "Motivational Speech": {"damage": (5, 15), "cost": 8, "effect": "inspiration"},
    }

    player_mana = 50  # Mana for casting spells

    # Turn-based battle
    def display_health():
        print(f"Player Health: {player_health} | Mana: {player_mana}")
        print(f"Office Worker Health: {office_worker_health}\n")

    def display_inventory():
        print("Inventory:")
        for item, count in inventory.items():
            print(f"{item}: {count}")
        print()

    def attack(attacker, defender, attack_range):
        attack_points = random.randint(*attack_range)
        defender_health = max(defender - attack_points, 0)
        return defender_health, attack_points

    def print_slow(text):
        for char in text:
            print(char, end="", flush=True)
            time.sleep(0.03)
        print()

    print("WELCOME TO THE RPG BATTLE OF THE OFFICE WORKER!\n")
    print("You: The Brave Employee")
    print(player_art)
    print("Versus")
    print("Mr. Biggly at his golden desk")
    print(office_worker_art)
    print_slow("The battle begins!\n")

    while player_health > 0 and office_worker_health > 0:
        # Display health status
        display_health()

        # Player's turn
        print_slow("It's your turn! Choose your action:")
        print("1. Attack")
        print("2. Defend")
        print("3. Use Spell")
        print("4. Inventory")
        choice = input("> ")

        if choice == "1":
            # Player attacks
            office_worker_health, attack_points = attack(
                player_health, office_worker_health, player_attack_range
            )
            print_slow(f"You attacked Mr. B for {attack_points} damage!")

        elif choice == "2":
            # Player defends
            print_slow("You brace yourself and reduce incoming damage by 50%!")

        elif choice == "3":
            # Use a spell
            print("Choose a spell:")
            for spell, details in spells.items():
                print(
                    f"{spell}: Damage {details['damage']}, Mana Cost {details['cost']}"
                )
            spell_choice = input("> ").title()

            if spell_choice in spells:
                if player_mana >= spells[spell_choice]["cost"]:
                    spell = spells[spell_choice]
                    player_mana -= spell["cost"]
                    damage = random.randint(*spell["damage"])
                    office_worker_health -= damage
                    print_slow(f"You cast {spell_choice} and dealt {damage} damage!")
                    if "effect" in spell and spell["effect"] == "freeze":
                        print_slow("Target is frozen and misses their next turn!")
                        continue  # Office worker skips a turn
                    elif "effect" in spell and spell["effect"] == "inspiration":
                        print_slow("You feel inspired! You heal for 10 health.")
                        player_health = min(100, player_health + 10)
                else:
                    print_slow("Not enough mana! You waste your turn.")

        elif choice == "4":
            # Inventory menu
            display_inventory()
            print("Choose an item to use:")
            item_choice = input("> ").title()

            if item_choice in inventory and inventory[item_choice] > 0:
                if item_choice == "Potion":
                    heal_amount = random.randint(15, 30)
                    player_health = min(100, player_health + heal_amount)
                    print_slow(
                        f"You used a Potion and healed for {heal_amount} health!"
                    )
                elif item_choice == "Coffee":
                    player_attack_range = (20, 30)
                    print_slow(
                        "You drank some Coffee! Your attacks will be stronger for the next turn!"
                    )
                elif item_choice == "Stapler":
                    damage = random.randint(10, 25)
                    office_worker_health -= damage
                    print_slow(f"You threw a Stapler at him, dealing {damage} damage!")

                inventory[item_choice] -= 1
            else:
                print_slow("Invalid item or none left! You waste your turn.")

        else:
            print_slow("Invalid choice, you waste your turn!")

        if office_worker_health <= 0:
            break

        # Office Worker's turn
        print_slow("\nMr. B prepares to retaliate!\n")
        if choice == "2":
            # Player defends - reduce damage
            player_health, attack_points = attack(
                office_worker_health, player_health, office_worker_attack_range
            )
            reduced_damage = attack_points // 2
            player_health += reduced_damage
            print_slow(
                f"Mr. B attacks you for {attack_points} damage, but you reduce it to {reduced_damage} damage!"
            )
        else:
            player_health, attack_points = attack(
                office_worker_health, player_health, office_worker_attack_range
            )
            print_slow(f"Mr. B attacks you for {attack_points} damage!")

        print()

    # End of battle
    if player_health <= 0:
        print_slow("You have been defeated... The Office Worker wins. GAME OVER.")
    else:
        print_slow("Congratulations! You defeated Mr. B! Victory is yours!")

    print("\nFinal Status:")
    display_health()
