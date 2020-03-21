""" Lesson 10: Classes, scope, and namespaces """

import sys

class Person(firstname,lastname,age):
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk():
        print(f“Hello, my name is {firstname} {lastname} and I’m {age} years old”)

def main():
    p = set(input("Enter your Firstname, Lastname & age separated by comas: "))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGot KeyboardInterrupt! Exiting...")
        sys.exit()
