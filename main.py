# main.py

import random
from datetime import timedelta

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
        self.supplies = 0
        self.coffee_inventory = 1
        self.time_per_day = 28800  # 8 hours in seconds
        self.morning_end_time = 14400  # Noon in seconds
        self.current_time = 0  # Start of the day at 6:00 AM
        self.coffee_buff_active = False
        self.pet_bonus_active = False
        self.crops_tended = 0

        # Daily limits
        self.petted_today = False  # Track if the companion has been petted today
        self.crops_tended_today = 0  # Track the number of times crops have been tended
        self.max_crops_tended = 3  # Maximum times crops can be tended per day

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
        print()

    def perform_action(self, choice):
        # Set constant time costs for actions
        action_costs = {
            "1": 300,  # Pet companion: 5 minutes
            "2": 600,  # Make coffee: 10 minutes
            "3": 1800  # Tend crops: 30 minutes
        }

        time_cost = action_costs.get(choice, 0)
        if self.coffee_buff_active:
            time_cost //= 2  # Halve time cost if coffee buff is active

        if choice == "1":
            if self.petted_today:
                print(f"\nYou've already spent time with {self.pet_name} today.\n")
                return
            print(f"\nYou spend a few moments petting {self.pet_name}.")
            if random.random() < 0.5:  # 50% chance for crop progress bonus
                print(f"{self.pet_name} seems to have inspired you! (+1 crop progress)\n")
                self.crops_tended += 1
            else:
                print(f"{self.pet_name} wags their tail happily.\n")
            self.petted_today = True
        elif choice == "2":
            if self.coffee_inventory > 0:
                self.coffee_inventory -= 1
                self.coffee_buff_active = True
                print("You brew a cup of coffee and sip it slowly. Your actions will cost less time for the rest of the day!\n")
            else:
                print("You're out of coffee beans!\n")
        elif choice == "3":
            if self.crops_tended_today >= self.max_crops_tended:
                print("\nYou've tended to the crops as much as you can this morning.\n")
                return
            self.crops_tended += 1
            self.crops_tended_today += 1
            print("You tend to the crops. (+1 crop progress)\n")
        else:
            print("Invalid choice. Try again.\n")
            return  # Do not deduct time for invalid choice

        self.current_time += time_cost
        self.print_current_time()

    def print_current_time(self):
        hours, remainder = divmod(self.current_time, 3600)
        minutes = remainder // 60
        am_pm = "AM" if hours < 12 else "PM"
        hours = hours if hours <= 12 else hours - 12
        print(f"Current time: {hours}:{minutes:02d} {am_pm}\n")

    # ----- MAIN LOOP -----

    def morning_loop(self):
        print(f"🌞 It’s a new morning on {self.farm_name}.")
        self.morning_flavor()

        while self.current_time < self.morning_end_time:
            print(f"Time remaining: {self.morning_end_time - self.current_time} seconds")
            self.show_actions()
            choice = input("Choose an action (1–3): ").strip()
            self.perform_action(choice)

        print("--- Morning Summary ---")
        print(f"Crops tended: {self.crops_tended}")
        print(f"Coffee used: {1 - self.coffee_inventory}")
        print(f"{self.pet_name} seems content.\n")
        print("🌤️ The sun climbs high above the hills...\n")

# ----- RUN -----

if __name__ == "__main__":
    game = FarmGame()
    game.welcome()
    game.morning_loop()
