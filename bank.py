from decimal import *
import time
import json
import os
import account 
import person

def mainloop():
    print("*****************************************")
    print("*********Welcome to Virtual Bank*********")
    print("*****************************************")
    print("[1]=====> Create a bank account")
    print("[2]=====> Login to your bank account")
    print("*****************************************")
    print("*****************************************")

    # Create or choose an account
    accountSelect = input("=====> ")

    if accountSelect == "1":
        print("Welcome to registery")
        fname = input("Input your first name: ")
        lname = input("Input your last name: ")
        age = int(input("Input your age (be at least 14 to create a vbank account): "))
        if age < 14 or age >= 120:
            print("Failed to create account. Starting over...")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            mainloop()

       
        password = input("Create a password: ")
        # Create the PERSON class
        person = person.Person(fname, lname, age, password)
        print("Account created successfully successfully!")

    elif accountSelect == "2":
        pass

    else:
        print("Invalid key: Choose 1 or 2 and q to exit.")

# Function to start banking.
def starting():
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
        exit()
        


mainloop()