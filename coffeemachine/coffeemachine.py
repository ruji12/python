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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_sufficient_resource(ingredients):
    is_enough=True
    for item in ingredients:
        if resources[item]< ingredients[item]:
            print(f"Sorry you have not enough {item}")
            return is_enough==False
    return is_enough



def process_coins():

    num_of_quarters=((int(input("How many quarters?:")))*0.25)
    num_of_dimes=((int(input("How many quartes?:")))*0.10)
    num_of_nickels=((int(input("How many quartes?:")))*0.05)
    num_of_penneies=((int(input("How many quartes?:")))*0.01)
    total_money=num_of_dimes+num_of_nickels+num_of_penneies+num_of_quarters
    if(total_money>=MENU[check_order]["cost"]):
        print(f"Here is your change ${total_money-MENU[check_order]['cost']} in change.")

        
        global profit
        profit+=MENU[check_order]['cost']

    else:
        print("Sorry  that's not enough money.Money refunded!")

    return num_of_quarters,num_of_dimes,num_of_nickels,num_of_penneies
def make_coffee(ingredients):
    for item in ingredients:
        resources[item] -=ingredients[item]
    print("Here is your coffee !Enjoy your drink.")


is_on=True

while is_on:
    check_order=input("What would you like?(espresso/latte/cappuccino):")
    if check_order=="off":
        is_on=False
    elif check_order=="report":
   
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}ml")
        print(f"Money:${profit}")
    else:
    
        if is_sufficient_resource(MENU[check_order]["ingredients"]):
            print("Please insert coins.")
            if process_coins():
                make_coffee(MENU[check_order]["ingredients"])
    

