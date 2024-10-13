import random

class Game:
    def __init__(self):
        self.location = "Shattered Plains"
        self.inventory = []
        self.highstorm_warning = False
        self.is_running = True
        self.enemies = {"chasmfiend": {"health": 20, "damage": 5}}
        self.current_enemy = None
        self.quest_item = None

    def play(self):
        print("Welcome to the Stormlight Archive Adventure!")
        print("You are a budding Knight Radiant. Navigate through Roshar and uncover its secrets.")
        while self.is_running:
            self.show_location()
            action = input("What do you want to do? ").lower()
            self.process_action(action)

    def show_location(self):
        if self.location == "Shattered Plains":
            print("\nYou stand on the Shattered Plains, a vast expanse of rocky terrain.")
            print("Paths lead to the 'south' (to a camp) and 'north' (to a chasm).")
            if self.highstorm_warning:
                print("A warning bell sounds! A highstorm is approaching!")
        elif self.location == "Camp":
            print("\nYou are at the camp of the Alethi. Soldiers bustle about.")
            print("You can go 'north' back to the Shattered Plains or 'talk' to a soldier.")
            if self.quest_item:
                print("You can also 'give' the quest item to the soldier.")
        elif self.location == "Chasm":
            print("\nYou peer into a dark chasm. There's a faint light below.")
            print("You can go 'south' back to the Shattered Plains or 'climb' down.")
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
            print("A chasmfiend lurks here! You can 'fight' it or 'flee' back to Urithiru.")

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
            self.current_enemy = "chasmfiend"
            print("A chasmfiend appears! Prepare for battle!")
        elif action == "read" and self.location == "Library":
            print("You read a book about the history of the Knights Radiant.")
        elif action == "fight" and self.current_enemy:
            self.fight_enemy()
        elif action == "flee" and self.current_enemy:
            print("You flee back to Urithiru, escaping the chasmfiend.")
            self.location = "Urithiru"
            self.current_enemy = None
        elif action == "give" and self.location == "Camp" and self.quest_item:
            print("You hand the quest item to the soldier. He thanks you!")
            self.quest_item = None
        elif action == "check inventory":
            self.show_inventory()
        elif action == "quit":
            print("Thanks for playing!")
            self.is_running = False
        else:
            print("I don't understand that command.")

    def talk_to_soldier(self):
        print("The soldier tells you about the upcoming highstorm.")
        if not self.quest_item:
            print("He mentions a lost artifact nearby. If you find it, he would reward you.")
            self.quest_item = "lost artifact"
        else:
            print("You have already talked to the soldier about the artifact.")

    def show_inventory(self):
        if self.inventory:
            print("Your inventory contains: " + ", ".join(self.inventory))
        else:
            print("Your inventory is empty.")

    def fight_enemy(self):
        if self.current_enemy == "chasmfiend":
            enemy_health = self.enemies[self.current_enemy]["health"]
            player_damage = random.randint(3, 7)
            enemy_damage = self.enemies[self.current_enemy]["damage"]

            print("You attack the chasmfiend!")
            enemy_health -= player_damage
            print(f"You deal {player_damage} damage! Chasmfiend's health is now {enemy_health}.")

            if enemy_health > 0:
                print("The chasmfiend retaliates!")
                print(f"It deals {enemy_damage} damage to you!")
            else:
                print("You have defeated the chasmfiend!")
                self.current_enemy = None

if __name__ == "__main__":
    game = Game()
    game.play()
