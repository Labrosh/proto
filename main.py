# main.py

import random

# ----- SETUP -----

# Action pool
actions_per_day = 3

class FarmGame:
    def __init__(self):
        # Game state
        self.day = 1
        self.farm_name = ""
        self.pet_type = ""
        self.pet_name = ""
        self.crop_progress = 0
        self.coffee_inventory = 1

    # ----- STARTUP -----

    def welcome(self):
        print("🌾 Welcome to your new life!\n")
        self.farm_name = input("What would you like to name your farm? ").strip()

        while True:
            pet_type_input = input("Do you want a dog or a cat? ").strip().lower()
            if pet_type_input in ["dog", "cat"]:
                self.pet_type = pet_type_input
                break
            print("Please choose 'dog' or 'cat'.")

        self.pet_name = input(f"What would you like to name your {self.pet_type}? ").strip()
        print(f"\n🌅 Day {self.day} — Morning at {self.farm_name}")
        print(f"{self.pet_name} the {self.pet_type} stretches lazily as you get out of bed.\n")

    # ----- MORNING FLAVOR -----

    def morning_flavor(self):
        options = [
            f"{self.pet_name} rolls onto their back, asking for belly rubs.",
            f"You hear {self.pet_name} rustling around the kitchen.",
            f"{self.pet_name} is watching the sunrise through the window.",
            f"{self.pet_name} lets out a dramatic yawn and climbs into your lap.",
            f"{self.pet_name} is chasing dust motes in the light.",
        ]
        print(random.choice(options))
        print()

    # ----- ACTIONS -----

    def show_actions(self):
        print("What would you like to do this morning?")
        print("1. Pet your companion")
        print("2. Make coffee")
        print("3. Tend to crops")
        print("4. Check supplies (no effect)")
        print()

    def perform_action(self, choice, state):
        if choice == "1":
            print(f"\nYou spend a few moments petting {self.pet_name}.")
            if random.random() < 0.5:
                print(f"{self.pet_name} nuzzles into your hand. You feel energized. (+1 bonus action!)\n")
                state["actions"] += 1
            else:
                print(f"{self.pet_name} wags their tail happily.\n")
        elif choice == "2":
            if self.coffee_inventory > 0:
                self.coffee_inventory -= 1
                print("You brew a cup of coffee and sip it slowly. (+1 bonus action!)\n")
                state["actions"] += 1
            else:
                print("You're out of coffee beans!\n")
        elif choice == "3":
            self.crop_progress += 1
            print("You water and tend to your crops. They look healthier. (+1 crop progress)\n")
        elif choice == "4":
            print("You check your shelves. Everything’s in its place. (no effect)\n")
        else:
            print("Invalid choice. Try again.\n")
            state["actions"] += 1  # Give back the action if they typo

    # ----- MAIN LOOP -----

    def morning_loop(self):
        state = {"actions": actions_per_day}
        print(f"🌞 It’s a new morning on {self.farm_name}.")
        self.morning_flavor()

        while state["actions"] > 0:
            print(f"Actions remaining: {state['actions']}")
            self.show_actions()
            choice = input("Choose an action (1–4): ").strip()
            state["actions"] -= 1
            self.perform_action(choice, state)

        print("--- Morning Summary ---")
        print(f"Crop progress: {self.crop_progress}")
        print(f"Coffee left: {self.coffee_inventory}")
        print(f"{self.pet_name} seems content.\n")
        print("🌤️ The sun climbs high above the hills...\n")

# ----- RUN -----

if __name__ == "__main__":
    game = FarmGame()
    game.welcome()
    game.morning_loop()
