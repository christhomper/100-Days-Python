from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of each machine component
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Main program loop
is_on = True
while is_on:
    # Get user input for drink choice
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")

    # Handle special commands
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        # Process drink order if available and resources/payment are sufficient
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)




