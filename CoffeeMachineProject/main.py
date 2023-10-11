MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
profit = 0


def query():
    get_in = input("What would you like? (espresso/latte/cappuccino):")
    return get_in


def report():
    water = resources['water']
    mike = resources['milk']
    coffee = resources['coffee']
    print(f"Water: {water}ml")
    print(f"Milk: {mike}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${profit}")


def check_sufficient(coffee):
    flag = True
    for key in resources:
        if resources[key] < MENU[coffee]["ingredients"][key]:
            print(f"Sorry there is not enough {key}")
            flag = False
    return flag


def calculate(q, d, n, p) -> float:
    money = q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
    return money


def pay():
    print("Please insert the coin.")
    quarter = int(input("quarter:"))
    dime = int(input("dime:"))
    nickle = int(input("nickle:"))
    penny = int(input("penny:"))
    money = calculate(q=quarter, d=dime, n=nickle, p=penny)
    return money


def check_money(money_re, coffee):
    money_cost = MENU[coffee]['cost']
    if money_re >= money_cost:
        change = round(money_re - money_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += money_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def consume(coffee):
    for key in resources:
        resources[key] -= MENU[coffee]["ingredients"][key]


if __name__ == '__main__':
    while True:
        user_in = query()
        # 退出
        if user_in == 'off':
            exit()
        # 打印日志
        elif user_in == 'report':
            report()
            continue
        # 检查资源是否足够
        if check_sufficient(user_in):
            money_received = pay()
            if check_money(money_received, coffee=user_in):
                print("Successful")
                consume(coffee=user_in)
                report()
                print(f"Here is your {user_in}. Enjoy!")
