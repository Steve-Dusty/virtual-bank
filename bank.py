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

    # PART ONE
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
        time.sleep(1)
        print("Confirm your information: ")
        print(f"First name: {fname}")
        print(f"Last name: {lname}")
        print(f"Age: {age}")
        print(f"Password: {password}")
        time.sleep(1)
        confirm = input("Is this information correct? (y/n): ").lower()
        if confirm == "y".lower():
            # Create the PERSON class
            persons = person.Person(fname, lname, age, password)
            persons.prepare_all()
            persons.write_fname()
            persons.write_lname()
            persons.write_age()
            persons.write_password()
            persons.write_balance()
            print("Account created successfully successfully!")
            time.sleep(0.5)
            input(f"Your new bank email is: {(fname + lname).lower()}@vbank.com. You will use this to login to your bank account... Enter to continue") 
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            mainloop()

        else: 
            os.system('cls' if os.name == 'nt' else 'clear')
            mainloop()


    # PART TWO
    elif accountSelect == "2":
        starting()

    # LAST PART
    else:
        print("Invalid key: Choose 1 or 2")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        mainloop()

# Function to start banking.
def starting():
    user = account.Account()
    while True:
        choices = input("Select: (1) Deposit (2) Withdraw (3) Get balance: ").lower()

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
                
        elif choices == "q".lower():
            print("Signing out...")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            mainloop()        


mainloop()