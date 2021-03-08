from decimal import *
import time
import json


class Person:
    def __init__(self, fname, lname, age, password):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.password = password
        self.email = (fname + lname + "@vbank.com").lower()


    def prepare_all(self):
        with open("accounts.json", "r") as f:
            account = json.load(f)
        account[self.email] = {}
        with open("accounts.json", "w") as f:
            #prepare_string = {self.email: {}}
            json.dump(account, f, indent=4)

    def write_fname(self):
        with open("accounts.json", "r") as f:
            account = json.load(f)
        account[self.email]["first_name"] = self.fname
        with open("accounts.json", "w") as f:
            json.dump(account, f, indent=4)
    
    def write_lname(self):
        with open("accounts.json", "r") as f:
            account = json.load(f)
        account[self.email]["last_name"] = self.lname
        with open("accounts.json", "w") as f:
            json.dump(account, f, indent=4)

    def write_age(self):
        with open("accounts.json", "r") as f:
            account = json.load(f)
        account[self.email]["age"] = self.age
        with open("accounts.json", "w") as f:
            json.dump(account, f, indent=4)

    def write_password(self):
        with open("accounts.json", "r") as f:
            account = json.load(f)
        account[self.email]["password"] = self.password
        with open("accounts.json", "w") as f:
            json.dump(account, f, indent=4)


