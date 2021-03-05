from decimal import *
import time
import json
import account 
import person


print("*****************************************")
print("*********Welcome to Virtual Bank*********")
print("*****************************************")
print("[1]=====> Create a bank account")
print("[2]=====> Login to your bank account")
print("*****************************************")
print("*****************************************")

accountSelect = input("=====> ")

if accountSelect == "1":
    pass

elif accountSelect == "2":
    pass

else:
    print("Invalid key: Choose 1 or 2.")
    
while True:
    user = account.Account()
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

