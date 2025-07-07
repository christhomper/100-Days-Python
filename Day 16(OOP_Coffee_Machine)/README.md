# ☕ Coffee Machine (OOP Version)

An object-oriented simulation of a coffee vending machine written in Python. This version expands on the procedural model by using classes to encapsulate responsibilities for the coffee menu, machine, and payment handling.

## ▶️ Features

- Object-oriented design using classes and methods
- Handles multiple drink types: latte, espresso, cappuccino
- Simulates coin payment and gives change
- Tracks resource availability (water, milk, coffee)
- Supports machine reporting and shutdown (`off`)
- Modular design with four separate files

## 📁 File Structure

- `app.py` – Entry point and control loop for the machine
- `menu.py` – Contains `Menu` and `MenuItem` classes for drink data and selection
- `coffee_maker.py` – Manages resources, checks sufficiency, and makes drinks
- `money_machine.py` – Processes coins, handles payment, and tracks profit

## 🧠 Concepts Practiced

- Object-Oriented Programming (OOP)
- Class attributes and methods
- Modularization and separation of concerns
- Input validation and conditional logic
- Resource and currency management

## 🔧 Commands

- `espresso`, `latte`, `cappuccino` – Order drinks
- `report` – See current resources and profit
- `off` – Shut down the machine

---