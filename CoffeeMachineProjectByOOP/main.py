from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    coffee_machine = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()
    while True:
        user_in = input(f"What do you want?{menu.get_items()}:")
        if user_in == 'off':
            exit()
        elif user_in == 'report':
            coffee_machine.report()
            money_machine.report()
            continue
        drink = menu.find_drink(user_in)
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)

