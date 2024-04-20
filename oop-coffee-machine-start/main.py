from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on =True



def getorder():
    global user_input
    user_input = input('What would you like? |espresso| |latte| |cappuccino|: ')
    return user_input

while True:
    print()
    getorder()
    end_order = input('Would you like to end order "y" or "n" or "report": ')
    if end_order == "y":
        break
    if end_order == "report":
        coffee_maker.report()
        money_machine.report()


def checkorder():
    time.sleep(1)
    print()
    print('ORDER PROCESSING... 🕑')
    print()
    
    drink = menu.find_drink(user_input)
    is_true = coffee_maker.is_resource_sufficient(drink)
    
    if is_true == True and money_machine.make_payment(drink.cost):
        time.sleep(2)
        print()
        print('ORDER RECEIVED ✅')
        print()
        time.sleep(2)
        coffee_maker.make_coffee(drink)
        print()
    else:
        print()
        time.sleep(2)
        print('ORDER DECLINED ❌')
        print()
        
checkorder()

