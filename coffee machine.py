from importlib.resources import is_resource
from statistics import median_low

menu={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":20,
        },
        "cost":25,
    },
    "lotte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":25,
        },
        "cost":30,
    },
    "cappuccino":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":30,
        },
        "cost":35,
    }
}
profit=0
resources={
    "water":500,
    "milk":400,
    "coffee":150,
}
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"sorry,there is no enough {item}")
            return False
    return True
def process_coins():
    print("please insert coins")
    coins=int(input("enter how many coins you process:"))
    total=int(input("1 rupee coin:"))*1
    total+=int(input("2 rupee coin:"))*2
    total+=int(input("5 rupee coin:"))*5
    total+=int(input("10 rupee coin:"))*10
    return total
def transaction_successful(received_money,drink_cost):
    if received_money>=drink_cost:
        change=received_money-drink_cost
        print(f"rupees{change} in change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("sorry that's not enough money,money refunded.")
        return False
def make_drink(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

is_on=True
while is_on:
    choice=input("what would you want:(espresso/lotte,cappuccino):")
    if choice == "off":
        break
    elif choice == "report":
        print("available resources:")
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"money:{profit}rupees")
    else:
        drink=menu[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment=process_coins()
            if transaction_successful(payment,drink['cost']):
                make_drink(choice, drink["ingredients"])


