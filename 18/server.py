from application import Application


if __name__ == "__main__":
    name = input("name? >")

    app = Application()
    res = res.run()

    if res == 0:
        print("Ended successfully")

