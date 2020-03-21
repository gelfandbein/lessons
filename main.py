#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:17:34 2020
@author: boris.gelfandbein@gmail.com
"""

import subprocess
import sys

try:
    import pyfiglet
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", 'pyfiglet'])
finally:
    import pyfiglet

    ### https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/ || digital, 3x5
    result = pyfiglet.figlet_format("B E E T R O O T   L E S S O N S", font="digital")
    print(result)


if __name__ == "__main__":
    pass
else:
    print("error!")
    brake

### define main variables
def lessons(keys, lesson_name):
    lessons = {1: "lesson01", 2: "lesson02", 3: "lesson03""}
    return lessons.keys()


#lessons = {1: 'lesson01', 2: 'lesson02', 3: 'lesson03'}

print(lessons(keys))
#print(lessons())

### we want number the lesson to run
def choice(message):
    while True:
        try:
            choice = input(message)
        except ValueError:
            print("Try again ;\)")
            continue
        else:
            return choice
            break


print(f"Hello! Now we have {len(lessons.keys())} lessons. q - to quit")
answer_main = choice("What lassons do you want to run?: ")

### work with answer from keyboard
if answer_main == lessons[1]:
    print(f"Thank you! You choose {answer_main}st lesson! Let's do it!")
    # exec('lesson01.py')
    # os.system('python3 lesson01.py')
elif answer_main == 2:
    print(f"Thank you! You choose {answer_main}nd lesson! Let's do it!")
    # os.system('python3 lesson02.py')
elif answer_main == 'q':
    print("quiting...")
else:
    print(f"You answer {answer_main} is wrong!")
    

print("bye!")