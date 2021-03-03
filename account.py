from decimal import *
import time
import json


class Account():
    def __init__(self):
        self.balance = 0
        self.withdraw = 0
    
    def deposits(self, deposit):
        self.balance += deposit

    def withdraws(self, withdraw):
        self.balance -= withdraw
    def get_balance(self):
        return self.balance

