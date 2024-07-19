from main import MENU,resources


machine_run = True
price = 0
def sufficient(coffee_chosen):
    for items in coffee_chosen:
        if coffee_chosen[items] >= resources[items]:
            print(f"Not enough {items} to make coffee")
            return False
    return True
def process_coins():
    quarter = int(input("How many quarters:")) * 0.25
    nickles = int(input("How many nickles:")) * 0.05
    dimes = int(input("How many dimes:")) * 0.10
    pennies = int(input("How many pennies:")) * 0.01

    value = quarter + nickles + dimes + pennies

    return value

def transaction(purchased, coffee_price): 
        if purchased >= coffee_price:
            change = round(purchased - coffee_price,2)
            if change == 0:
                print("No change")
            else:
                print(f"Your change is {change}")
            global price
            price = price + coffee_price
            return True
        else:
            print("Insufficient funds, Money refunded")
            return False

def make_coffee(coffee_name,coffee):
    for item in coffee:
        resources[item] -= coffee[item]
        print(f"Here is your {coffee_name}😎")
        



while machine_run:
    
    coffee_type = input("What would you like? (espresso/latte/cappuccino) : ")

    if coffee_type == "report":
        print(f"water:{resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
    elif coffee_type == "off":
        machine_run = False
    else:
        coffee = MENU[coffee_type]
        if sufficient(coffee["ingredients"]):
            cash = process_coins()
            if transaction(cash,coffee["cost"]):
                make_coffee(coffee_type,coffee["ingredients"])






    
    
 
    
                

        







