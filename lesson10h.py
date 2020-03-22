# Lesson 10: Classes, scope, and namespaces
import sys


class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        return print(f"Hello, my name is {self.firstname} {self.lastname}. I'm {self.age} years old")

def main():
    a, b, c = input("Enter yours Firstname, Lastname & age separated by space: ").split()
    Person(a,b,c)
    Person.talk()


if __name__ == "__main__":
    try:
        main()
        #app = Person()
    except KeyboardInterrupt:
        print("\nGot KeyboardInterrupt! Exiting...")
        sys.exit()
