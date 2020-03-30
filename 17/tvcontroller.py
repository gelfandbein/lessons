# Lesson 17: Test cases

import sys

class TVController():
    def __init__(self):
        self.list = ["BBC", "Discovery", "TV1000"]
        self.status = 0
        self.channel = 0

    def test(self):
        if self.status == 0:
            status = input("Yours TV is turned 0FF. Turn it 0N? (y/n): ")
            if status == "y":
                return print("Hardware test passed!")
            else:
                raise KeyboardInterrupt


    def swith(self, channel):
        if channel == len(self.list):
            self.channel = 0
        elif channel < 0:
            self.channel = len(self.list)-1
        
        print(f"-> '{self.list[self.channel]}' channel found. Switching...")
        controller.main()

    def main(self):
        print(f"Now you watch the {self.list[self.channel]} channel. You have {self.list} channels.")
        choice = input("Do you want switch the channel? (p)revious or (n)ext (q - to quit): ")
        if choice == "n":
            self.channel = self.channel + 1
            controller.swith(self.channel)
        elif choice == "p":
            self.channel = self.channel - 1
            controller.swith(self.channel)
        else:
            raise KeyboardInterrupt


if __name__ == "__main__":
    controller = TVController()
    try:
        controller.test()
        controller.main()
    except KeyboardInterrupt:
        print("\nGot STOP. Turning 0FF & exiting from this fucking world...")
        sys.exit()
