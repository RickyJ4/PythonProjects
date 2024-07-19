from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_machine = True

while coffee_machine:
    name = input("What would you like? (espresso/latte/cappuccino) : ")
    

    if name == "report":
         CoffeeMaker.report(name)
    elif name == "off":
        coffee_machine = False
    else:
        Menu.find_drink(name)
        if CoffeeMaker.is_resource_sufficient(name):
            cost = MoneyMachine.make_payment(name)
            if MenuItem[cost]:
                CoffeeMaker.make_coffee(name)
