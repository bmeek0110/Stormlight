import random

class Game:
    def __init__(self):
        self.player_health = 30
        self.location = "Shattered Plains"
        self.inventory = []
        self.highstorm_warning = False
        self.is_running = True
        self.enemies = {
            "chasmfiend": {"health": 25, "damage": 5},
            "voidbringer": {"health": 30, "damage": 7}
        }
        self.current_enemy = None
        self.quests = {
            "lost_artifact": {"completed": False, "description": "Find the lost artifact.", "location": "Chasm"},
            "rescue_soldier": {"completed": False, "description": "Rescue a soldier trapped in the Chasm.", "location": "Chasm"}
        }
        self.shelter_found = False

    def play(self):
        print("Welcome to the Stormlight Archive Adventure!")
        print("You are a budding Knight Radiant. Navigate through Roshar and uncover its secrets.")
        while self.is_running:
            self.show_status()
            self.show_location()
            action = input("What do you want to do? ").lower()
            self.process_action(action)

    def show_status(self):
        print(f"\nYour health: {self.player_health}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")
        for quest, details in self.quests.items():
            status = "Completed" if details["completed"] else "In Progress"
            print(f"{quest.capitalize()}: {status}")

    def show_location(self):
        if self.location == "Shattered Plains":
            print("\nYou stand on the Shattered Plains, a vast expanse of rocky terrain.")
            print("Paths lead to the 'south' (to a camp) and 'north' (to a chasm).")
            if self.highstorm_warning:
                print("A warning bell sounds! A highstorm is approaching!")
        elif self.location == "Camp":
            print("\nYou are at the camp of the Alethi. Soldiers bustle about.")
            print("You can go 'north' back to the Shattered Plains, 'talk' to a soldier, or check for 'quests'.")
            if "lost artifact" in self.inventory:
                print("You can also 'give' the lost artifact to the soldier.")
        elif self.location == "Chasm":
            print("\nYou peer into a dark chasm. There's a faint light below.")
            print("You can go 'south' back to the Shattered Plains or 'climb' down.")
            if self.quests["rescue_soldier"]["completed"]:
                print("You have rescued the soldier!")
        elif self.location == "Urithiru":
            print("\nYou have entered the ancient city of Urithiru, filled with secrets.")
            print("Explore 'north' (the library) or 'south' (the tower).")
        elif self.location == "Library":
            print("\nThe library is filled with tomes and scrolls. Knowledge is abundant.")
            print("You can go 'south' back to Urithiru or 'read' a book.")
        elif self.location == "Tower":
            print("\nYou stand at the base of a towering structure. It's intimidating.")
            print("You can go 'north' back to Urithiru or 'climb' the tower.")
        elif self.location == "Chamber":
            print("\nYou've entered a hidden chamber in the tower.")
            if self.current_enemy:
                print(f"A {self.current_enemy} lurks here! You can 'fight' it or 'flee' back to Urithiru.")
            else:
                print("The chamber is empty, but there seems to be a faint glow in the corner.")

    def process_action(self, action):
        if action == "go south" and self.location == "Shattered Plains":
            self.location = "Camp"
        elif action == "go north" and self.location == "Camp":
            self.location = "Shattered Plains"
        elif action == "go north" and self.location == "Chasm":
            self.location = "Shattered Plains"
        elif action == "go south" and self.location == "Chasm":
            print("It's too dangerous to go that way!")
        elif action == "climb down" and self.location == "Chasm":
            print("You climb down and find a small group of sprens.")
            self.inventory.append("sprens")
            print("You have collected some sprens!")
        elif action == "talk" and self.location == "Camp":
            self.talk_to_soldier()
        elif action == "go north" and self.location == "Urithiru":
            self.location = "Library"
        elif action == "go south" and self.location == "Library":
            self.location = "Urithiru"
        elif action == "go south" and self.location == "Tower":
            self.location = "Urithiru"
        elif action == "climb" and self.location == "Tower":
            print("You climb the tower and discover a hidden chamber!")
            self.location = "Chamber"
            self.current_enemy = random.choice(list(self.enemies.keys()))
            print(f"A {self.current_enemy} appears! Prepare for battle!")
        elif action == "read" and self.location == "Library":
            print("You read a book about the history of the Knights Radiant.")
        elif action == "fight" and self.current_enemy:
            self.fight_enemy()
        elif action == "flee" and self.current_enemy:
            print("You flee back to Urithiru, escaping the enemy.")
            self.location = "Urithiru"
            self.current_enemy = None
        elif action == "give" and self.location == "Camp" and "lost artifact" in self.inventory:
            print("You hand the lost artifact to the soldier. He thanks you and rewards you!")
            self.inventory.remove("lost artifact")
            self.quests["lost_artifact"]["completed"] = True
        elif action == "quests":
            self.show_quests()
        elif action == "quit":
            print("Thanks for playing!")
            self.is_running = False
        else:
            print("I don't understand that command.")

    def talk_to_soldier(self):
        print("The soldier tells you about the upcoming highstorm.")
        if "lost artifact" not in self.inventory:
            print("He mentions a lost artifact nearby. If you find it, he would reward you.")
            self.inventory.append("lost artifact")
        else:
            print("You have already talked to the soldier about the artifact.")

    def show_quests(self):
        for quest, details in self.quests.items():
            status = "Completed" if details["completed"] else "In Progress"
            print(f"{quest.capitalize()}: {details['description']} - Status: {status}")

    def fight_enemy(self):
        enemy_health = self.enemies[self.current_enemy]["health"]
        while self.player_health > 0 and enemy_health > 0:
            player_damage = random.randint(5, 10)
            enemy_damage = self.enemies[self.current_enemy]["damage"]

            # Player attack
            enemy_health -= player_damage
            print(f"You attack the {self.current_enemy} and deal {player_damage} damage!")
            print(f"{self.current_enemy}'s health is now {enemy_health}.")

            if enemy_health > 0:
                # Enemy attack
                self.player_health -= enemy_damage
                print(f"The {self.current_enemy} attacks you and deals {enemy_damage} damage!")
                print(f"Your health is now {self.player_health}.")
        
        if enemy_health <= 0:
            print(f"You have defeated the {self.current_enemy}!")
            self.current_enemy = None
        elif self.player_health <= 0:
            print("You have been defeated. Game over!")
            self.is_running = False

if __name__ == "__main__":
    game = Game()
    game.play()
