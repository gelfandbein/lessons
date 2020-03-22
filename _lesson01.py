#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:27:17 2020

@author: boris
"""

### we want number the task to run
#choice01 = ()
def choice01(message):
    while True:
        try:
            choice01 = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return choice01
            break

answer01 = choice01("Select task from 2 to 3: ")

if answer01 == 2:
    print("""
    Create a python program named “task2”, and use the built-in function `print` in it several times.
    Try to pass “sep”, “end” params and pass several parameters separated by commas. 

    Also, provide a comment text above each print statement, mentioned above,
    with the expected output after execution of the particular print statement.
    
    """)

    print("This", "is","text","with","separator=","and","end=",sep=' # ',end='@')
elif answer01 == 3:
    print("Task 3")
    pass
else:
    print('Wrong choice')
    exit(1)
    
    