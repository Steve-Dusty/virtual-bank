from decimal import *
import time
import json


class Account():


    @staticmethod
    def deposits(deposit, email):
        with open("accounts.json", "r") as f:
            account = json.load(f)
        account[email]["balance"] == deposit 
        with open("accounts.json", "w") as f:
            json.dump(account, f, indent=4)

    @staticmethod
    def withdraws(withdraw):
        with open("accounts.json", "r") as f:
            deposit = json.load(f)
        deposit["deposit"] -= withdraw
        with open("accounts.json", "w") as f:
            json.dump(deposit, f, indent=4)

    @staticmethod
    def get_balance():
        with open("accounts.json", "r") as f:
            balance = json.load(f)
            return balance["deposit"]
    


    
