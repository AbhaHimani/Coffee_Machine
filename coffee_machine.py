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
cont = True
def is_resource_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item]>resources[item]:

            print(f"Sorry there isn't enough {item}")
            return False
    return True
def is_money_sufficient(money, cost):
    if money>cost:
        print("Transaction successful! Here's your drink")
        to_be_returned= round(money-cost)
        print(f" Amount to be returned {to_be_returned}")
    else:
        print("Oops, you don't have enough money")
def left_resources (order_ingredients):
    for item in order_ingredients:
        resources[item]= (resources[item]) - int(order_ingredients[item])
while cont == True:
 want = input("What would you like? latte/cappuccino/espresso?")
 if want == "OFF":
    cont = False
 elif want == "report":
     print(resources["water"])
     print(resources["milk"])
     print(resources["coffee"])
 else:
     drink= MENU[want]
     if is_resource_sufficient(drink["ingredients"])==True:
         quarters=int(input("Enter your quarters:"))
         dimes=int(input("Enter your dimes:"))
         nickles=int(input("Enter your nickles:"))
         pennies=int(input("Enter your pennies:"))
         total_money = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
         is_money_sufficient(total_money, drink["cost"])
         left_resources(drink["ingredients"])











