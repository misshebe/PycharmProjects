#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

import time
user,passwd = 'ashe','666'

def auth(func):
    def wrapper(*args,**kwargs):
        username = input("Username:").strip()
        password = input("Password:").strip()

        if user == username and passwd == password:
            print("\033[32;1mUser has passed authentcation\033[0m")
            func(*args,**kwargs)
        else:
            exit("\033[31;1mInvalid username or password!\033[0m")
        return wrapper


def index():
    print("Welcome to index page")
@auth
def home():
    print("Welcome to home page ")
@auth
def bbs():
    print("Welcome to bbs page")

index()
home()
bbs()

