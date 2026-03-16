import time
import csv


def get_input(display_message):
    while True:
        try:
            float_value = float(input(display_message))
            break
        except ValueError:
            print("\033[0;31mInvalid input. Please enter a valid number.\033[0m")
    
    return float_value


def data_collection(state_massge, Amount, currentMoney):
    Time.append(time.strftime("%Y-%m-%d %I:%M:%S %p", time.localtime()))
    state.append(state_massge)
    amount.append(Amount)
    current_money.append(currentMoney)



Time = []
state = []
amount = []
current_money = []

budget = get_input("What is your budget? ")
data_collection("initial budget", budget, budget)

while True:
    table = zip(Time, state, amount, current_money)
    current_budget = current_money[-1]
    
    if current_budget < 20:
        print("\033[0;35mYour budget is too low. Please enter a budget of at least $20.\033[0m")
    
    stat = input("what you do (a/s/c/k/d/q)? ")

    if stat == 'a':
        money = get_input("How much money do you want to add? ")
        current_budget = current_budget + money
        data_collection("additional money", money, current_budget)
        print(f"\033[0;32mYour current budget is: {current_budget}\033[0m")

    
    elif stat == 's':
        money = get_input("How much money do you want to spend? ")
        current_budget = current_budget - money
        data_collection("spend money", money, current_budget)
        print(f"\033[0;33mYour current budget is: {current_budget}\033[0m")

    elif stat == 'c':
        print(f"\033[0;34mYour current budget is: {current_budget}\033[0m")
        

    elif stat == 'k':
        money = get_input("What is the correct amount of money in your account? ")
        correction = money - current_budget
        current_budget = current_budget + correction
        data_collection("account correction", correction , current_budget)
        print(f"\033[0;34mYour current budget is: {current_budget}\033[0m")


    elif stat == 'd':
        print("Time\t\t\tState\t\tAmount\tCurrent Money")
        for row in table:
            print("\t".join(str(x) for x in row))
    
    elif stat == 'q':
        with open("data.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(table)
        print("Goodbye!")
        break
