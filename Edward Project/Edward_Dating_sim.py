# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 12:45:37 2018

@author: Kieran O'Connor
"""
# import random
# import time
# these two I will uncomment if we decide to use them (time will let us put delays between the printing of lines)
import Control as c
# imports the most important variables all the files can access, LP + day count right now, more can be added easy
import School_Level as s
# imports the School level, this keeps the main sim file short and makes adding more levels easier
name = ""
# global variable to store the player's name
counter = 0
# global variable to keep track of the player's progress through the assignment table (game levels)


def lose():
        # this function is called when a player makes a bad choice
        print("You Lose\nEdward will never love you")
        print("You will now restart the Game")
        choose_name()


def win():
    # after every choice is answered correctly, this method is called
    global name
    # global counter
    print("Edward is taken aback, but finds himself pulled towards your lips. You kiss and sparks fly")
    print("Congratulations", name)
    print(
        "You have won the heart of our beloved Edward."
        "\nHe has succumbed to your seduction, and will now be your faithful lover")
    # counterInc()


def choose_name():
    # this method is to define the name variable and then increase the counter variable
    global counter
    global name
    name = input("Please enter your name\n")
    if name.lower() == "edward" or name.lower() == "ed":
        print("ur not Edward")
    elif name.lower() == "your name":
        print("Very Funny....")
        name = "Dad"
        print("Hello", name)
        counter = 1
    else:
        print("Hello", name)
        counter = 1


def school():
    global counter
    while c.day <= 5:
        if c.day == 1:
            s.day1()
        if c.day == 2:
            s.day2()
        if c.day == 3:
            s.day3()
        if c.day == 4:
            s.day4()
        if c.day == 5:
            s.day5()
        c.day += 1
        print("TESTING LovePoints Outside: " + str(c.LP))
    counter = 2


# this dictionary is used in order to corresponding functions to call for each counter values
# this is used as a cleaner alternative to recursion,
# while also allowing additional choices to be added relatively easily

assignmentTable = {
        0: choose_name,
        1: school,
        }
# the program will constantly loop, checking what method should be called for the current counter value
# this way it will always return here before continuing,
# making this a good place to add flags/variable print outs to check progress.
while True:
    func = assignmentTable.get(counter)
    func()
    if counter > 5:
        break
