from decimal import *
import time
import json
import account 



user = account.Account()


while True:
    choices = input("Select: (1) Deposit (2) Withdraw (3) Get balance: ")

    if choices == "1": 
        deposit = float(input("Input the amount: "))
        user.deposits(deposit)
        print(f"Your new balance is ${user.get_balance()}")

    elif choices == "2":
        withdraw = float(input("Input the amount: "))
        user.withdraws(withdraw)
        print(f"Your new balance is ${user.get_balance()}")

    elif choices == "3":
        print(f"Your balance is ${user.get_balance()}")
        

    elif choices == "q":
        print("You've been signed out")
        break

