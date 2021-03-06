from decimal import *
import time
import json

class Person:
    def __init__(self, fname, lname, age, password):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.password = password
        self.email = fname + lname + "@vbank.com"
        self.fullname = fname + " " + lname


    def write_email(self):
        with open("accounts.json", "w") as f:
            json.dump(self.email, f, indent=4)

    def write_fullname(self):
        pass

    def write_age(self):
        pass

    def write_password(self):
        pass

