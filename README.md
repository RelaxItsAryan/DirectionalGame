# Python Adventure Game

## 📖 Overview

This is a simple **text-based adventure game** written in Python. The player explores different rooms, collects items, and faces random enemies. The goal is to survive as long as possible while exploring.

---

## 🚀 Features

* Explore different rooms (forest, river, cave)
* Collect useful items (torch, rope, sword)
* Random enemy encounters (wolf, bandit, goblin)
* Simple combat system (fight with sword or take damage)
* Player health and inventory tracking

---

## 🛠️ Requirements

* Python 3.x
* No external libraries needed (only uses built-in Python modules: `time`, `random`, `sys`)

---

## ▶️ How to Play

1. Clone or download this repository.
2. Run the script in your terminal:

   ```bash
   python adventure.py
   ```
3. Enter your name when prompted.
4. Use commands to play the game.

---

## 🎮 Commands

* Movement: `north`, `south`, `east`, `west`
* Collect items: `take <item>` (example: `take torch`)
* Quit game: `quit`

---

## 🕹️ Example Gameplay

```text
Welcome to the Python Adventure!
What is your name, adventurer? Aryan

Greetings, Aryan. Your journey begins...

Aryan - Health: 100
Inventory: Empty

You are in a dark forest clearing.
You see: torch
Available exits: north

What will you do? take torch
You picked up the torch.
```

---

## ⚔️ Enemy Encounters

* At random times, enemies (wolf, bandit, goblin) may attack.
* If you have the **sword**, you can fight them off.
* If not, you will take damage (10–30 HP).

---

## 🏁 Game Over

* The game ends if your health drops to `0` or if you choose to `quit`.

---

## 📌 Future Improvements

* Add more rooms and items
* Implement a proper battle system
* Add puzzles or quests
* Save/load progress

---

👨‍💻 Made with ❤️ in Python.
