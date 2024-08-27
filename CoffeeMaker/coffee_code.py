MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def drink_choice(resources_present, money_present=0):
    while True:
        user_drink = input("What would you like? (espresso/latte/cappuccino/report): ")
        if user_drink == 'report':
            print(f"Water: {resources_present['water']}ml")
            print(f"Milk: {resources_present['milk']}ml")
            print(f"Coffee: {resources_present['coffee']}g")
            print(f"Money: ${money_present}")
        elif user_drink in ['espresso', 'latte', 'cappuccino']:
            return user_drink
        else:
            print("Invalid selection. Please try again.")


def coins():
    print("Please insert coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total_amount = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    total_amount = round(total_amount, 2)
    print(f"Total amount inserted: ${total_amount}")
    return total_amount


def ingredients(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_transaction(drink_chosen_by_user, inserted_amount):
    cost = MENU[drink_chosen_by_user]["cost"]
    if inserted_amount >= cost:
        change = round(inserted_amount - cost, 2)
        print(f"Here is ${change} in change.")
        global money_present
        money_present += cost
        for item in MENU[drink_chosen_by_user]["ingredients"]:
            resources[item] -= MENU[drink_chosen_by_user]["ingredients"][item]
        print(f"Here is your {drink_chosen_by_user}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


def drink():
    global money_present
    money_present = 0
    while True:
        user_drink = drink_choice(resources, money_present)
        if ingredients(MENU[user_drink]["ingredients"]):
            inserted_amount = coins()
            process_transaction(user_drink, inserted_amount)


# Start the process
drink()
