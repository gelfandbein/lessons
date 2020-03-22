import sys







if __name__ == "__main__":
    dog_age = int(input("Enter dog's age to transform in human: "))
    app = Dog(dog_age)
    try:
        app.human_age()
    except KeyboardInterrupt:
        print("\nGot KeyboardInterrupt! Exiting...")
        sys.exit()
