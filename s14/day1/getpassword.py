#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

#import getpass

_username = "surface"
_password = "shagua"

username = input("username:")
#password = getpass.getpass("password")
password = input("password:")

if _username == username and _password == password:
    print ("Welcome user {name} login...".format(name=username))
else:
    print ("Invalid username or password!")
