# Lesson 10: Classes, scope, and namespaces
# Task 1: A Person class

import sys


class Person():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {app.firstname} {app.lastname} & i'm {app.age} years old")


if __name__ == "__main__":
    a, b, c = input("Enter yours Firstname, Lastname & age separated by space: ").split()
    app = Person(a, b, c)
    try:
        app.talk()
    except KeyboardInterrupt:
        print("\nGot KeyboardInterrupt! Exiting...")
        sys.exit()
