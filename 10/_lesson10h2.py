# Lesson 10: Classes, scope, and namespaces
# Task 2: Doggy age

import sys


class Dog():
    def __init__(self, dog_age):
        self.age_factor = int("7")
        self.dog_age = dog_age

    def human_age(self):
        print(f"Human age: {app.age_factor * app.dog_age}")


if __name__ == "__main__":
    dog_age = int(input("Enter dog's age to transform in human: "))
    app = Dog(dog_age)
    try:
        app.human_age()
    except KeyboardInterrupt:
        print("\nGot KeyboardInterrupt! Exiting...")
        sys.exit()
