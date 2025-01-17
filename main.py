from art import  logo,banner

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
print( logo )
print(banner)
espresso_q = [MENU['espresso']['ingredients']['water'], MENU['espresso']['ingredients']['coffee']]
latte_q = [MENU['latte']['ingredients']['water'], MENU['latte']['ingredients']['milk'], MENU['latte']['ingredients']['coffee']]
cappuccino_q = [MENU['cappuccino']['ingredients']['water'], MENU['cappuccino']['ingredients']['milk'], MENU['cappuccino']['ingredients']['coffee']]

def process_coin():
    penny = 0.01
    dime = 0.10
    nickel = 0.05
    quarter = 0.25

    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))
    sum_coins = (quarters * quarter) + (dimes * dime) + (nickels * nickel) + (pennies * penny)
    return sum_coins


def check_enough_money(user_choice, sums):
    left_money = 0
    if user_choice == 'espresso':
        if sums >= 1.5:
            left_money = sums - 1.5
            return left_money
        else:
            return f"Sorry it not enough money. The amount {sums} is refunded "
    elif user_choice == 'latte':
        if sums >= 2.5:
            left_money = sums - 2.5
            return left_money
        else:
            return f"Sorry it not enough money. The amount {sums} is refunded "
    elif user_choice == 'cappuccino':
        if sums >= 3:
            left_money = sums - 3
            return left_money
        else:
            return f"Sorry it not enough money. The amount {sums} is refunded "

def deduct_after_making_coffee(espresso,latte,cappuccino, choice_of_user):
    global water, coffee, milk, total_balance
    if choice_of_user == 'espresso':
        water -= espresso[0]
        coffee -= espresso[1]
        total_balance+=1.5
    elif choice == 'latte':
        water -= latte[0]
        milk -= latte[1]
        coffee -=  latte[2]
        total_balance += 2.5
    else:
        water -= cappuccino[0]
        milk -= cappuccino[1]
        coffee -= cappuccino[2]
        total_balance += 3

def check_resources(drink):
    global water,coffee,milk
    if drink == 'espresso':
        if  water < 50  :
            return  "There is no enough water."
        elif coffee < 18 :
            return "There is no enough coffee."
    elif drink == 'latte':
        if  water < 200  :
            return "There is no enough water."
        elif  coffee < 24 :
            return "There is no enough coffee."
        elif milk < 150 :
            return "There is no enough milk."
    else :
        if  water < 250:
            return "There is no enough water."
        elif coffee < 24:
            return "There is no enough coffee."
        elif  milk < 100:
            return "There is no enough milk."


def report(water_q, milk_q, coffee_q, money):
    print( f"The resources are : \n 1-water : {water_q} lm\n 2-milk : {milk_q} lm\n 3-coffee : {coffee_q} g\n 4-balance : ${money:.2f}")

water = resources['water']
milk = resources['milk']
coffee = resources['coffee']

total_balance=0
while True:
# TODO: 1. Asking the user which type of drink
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino):").lower()
        if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino' or choice == 'off' or choice == 'report' :
            break
        else:
            print("Invalid input please try again")


    if choice == 'off':
        break
    elif choice == 'report':
        report(water , milk, coffee, total_balance)
    else :
        check = check_resources(choice)
        if check != "There is no enough water." and check != "There is no enough coffee." and check != "There is no enough milk.":
            print("please insert coins.")
            coins = process_coin()
            change = check_enough_money(choice, coins)
            if change != f"Sorry it not enough money. The amount {coins} is refunded ":
                print(f"Here is the changes : {round(change,2)}")
                print(f"Here is your {choice} ☕️. Enjoy!")
                deduct_after_making_coffee(espresso_q, latte_q, cappuccino_q, choice)
            else:
                print(change)

        else:
            print(check)






    ## if they input a report the machine should give a report about the resources left and money in
    ## if they input a wrong input they should be prompt that it is invalid and they should be able to input again
    ## if Check if the resources are enough to make a drink
        ## if yes make a coffee
            ## else prompt him that there is no enough resources

# TODO: 2. printing for inserting a coins and Taking input of 4 type of coins
    ## penny 0.01, dime 0.10, nickel 0.05, quarter 0.25




# TODO: 3. processing coins
   ## calculate the sum of all inputs
   ## check if they are enough for buying a drink 1.5 , 2.5 , 3
   ## if they are enough calculate subtract the input money to give him a changes
# TODO: 4. Make a coffee
  ## after making a coffee deduct from the current resources
