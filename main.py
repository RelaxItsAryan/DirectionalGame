import time
import random
import sys

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def show_status(self):
        print(f"\n{self.name} - Health: {self.health}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")

class Game:
    def __init__(self):
        self.rooms = {
            "start": {"desc": "You are in a dark forest clearing.", "items": ["torch"], "exits": {"north": "river"}},
            "river": {"desc": "A rushing river blocks your path.", "items": ["rope"], "exits": {"south": "start", "east": "cave"}},
            "cave":  {"desc": "A dark, damp cave with strange noises.", "items": ["sword"], "exits": {"west": "river"}},
        }
        self.current_room = "start"
        self.player = None

    def intro(self):
        print("Welcome to the Python Adventure!")
        name = input("What is your name, adventurer? ")
        self.player = Player(name)
        print(f"Greetings, {name}. Your journey begins...\n")
        time.sleep(1)

    def show_room(self):
        room = self.rooms[self.current_room]
        print(f"\n{room['desc']}")
        if room["items"]:
            print("You see:", ", ".join(room["items"]))
        print("Available exits:", ", ".join(room["exits"].keys()))

    def get_command(self):
        return input("\nWhat will you do? ").strip().lower()

    def move(self, direction):
        room = self.rooms[self.current_room]
        if direction in room["exits"]:
            self.current_room = room["exits"][direction]
            print(f"You move {direction}.")
        else:
            print("You can't go that way.")

    def take_item(self, item):
        room = self.rooms[self.current_room]
        if item in room["items"]:
            self.player.inventory.append(item)
            room["items"].remove(item)
            print(f"You picked up the {item}.")
        else:
            print(f"There is no {item} here.")

    def encounter_enemy(self):
        if random.random() < 0.3:
            enemy = random.choice(["wolf", "bandit", "goblin"])
            print(f"A {enemy} attacks!")
            if "sword" in self.player.inventory:
                print(f"You fight off the {enemy} with your sword!")
            else:
                damage = random.randint(10, 30)
                self.player.health -= damage
                print(f"The {enemy} injures you! You lose {damage} health points.")

    def game_loop(self):
        while self.player.health > 0:
            self.player.show_status()
            self.show_room()
            self.encounter_enemy()
            if self.player.health <= 0:
                break
            command = self.get_command()
            parts = command.split()
            if not parts:
                continue
            verb = parts[0]
            if verb in ["north", "south", "east", "west"]:
                self.move(verb)
            elif verb == "take" and len(parts) > 1:
                self.take_item(parts[1])
            elif verb == "quit":
                print("You decided to end your journey.")
                break
            else:
                print("I don't understand that command.")
        print("Game Over!")

if __name__ == "__main__":
    game = Game()
    game.intro()
    game.game_loop()
