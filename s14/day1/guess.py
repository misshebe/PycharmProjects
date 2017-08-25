#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

age_of_oldboy = 56

count =0

while count <3:
    guess_age =  int(input ("guess age:"))

    if guess_age == age_of_oldboy :
        print("yes,you got it")
        break
    elif guess_age > age_of_oldboy :
        print ("think small")
    else:
        print("think bigger!")

    count +=1

    if count == 3:
        countine_confirm = input ("Do you want to keep guessing?")
        if countine_confirm != 'n' :
            count = 0