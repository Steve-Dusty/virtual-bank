from decimal import *
import time
import json


class Account():
    def __init__(self):
        self.balance = 0
        self.withdraw = 0
    
    def deposits(self, deposit):
        with open("accounts.json", "w") as f:
            deposit_string = {"deposit":deposit}
            json.dump(deposit_string, f, indent=4)

    def withdraws(self, withdraw):
        with open("accounts.json", "r") as f:
            deposit = json.load(f)
        deposit["deposit"] -= withdraw
        with open("accounts.json", "w") as f:
            json.dump(deposit, f)

    def get_balance(self):
        with open("accounts.json", "r") as f:
            balance = json.load(f)
            return balance["deposit"]
    


    
