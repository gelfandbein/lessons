##
# Lesson 17: Test test cases
##
import sys

class TVController:
    def __init__(self):
        self.name = "My TVController"
        self.list = ["BBC", "Discovery", "TV1000"]
        self.status = 0
        self.channel = 0

    def test(self):
        if self.status == 0:
            ss = input("Yours TV is turned 0FF. Turn it 0N? (y/n): ")
            if ss == "y" or "yes":
                self.status = 1
                return print("Hardware test passed!")
            else:
                self.status = 0
                self.exit(True)


    def switch(self, channel):
        if channel == len(self.list):
            self.channel = 0
        elif channel < 0:
            self.channel = len(self.list)-1
        
        return self.main()

    def main(self):
        self.test()

        a = "\033[92m" + ', '.join(self.list) + "\033[0m"
        aa = "\x1b[1;31m" + ''.join(self.list[self.channel]) + "\033[0m"

        print("Now you watch the " + aa + " channel. You have " + a + " channels.")
        choice = input("Do you want switch the channel? (\033[1mp\033[0m)revious or (\033[1mn\033[0m)ext (q - to quit): ")
        if choice == "n":
            self.channel = self.channel + 1
            self.switch(self.channel)
        elif choice == "p":
            self.channel = self.channel - 1
            self.switch(self.channel)
        else:
            sys.exit(0)


if __name__ == "__main__":
    controller = TVController()
    try:
        controller.main()
    except:
        print("\nGot STOP. Turning 0FF & exiting from this fucking world...")
        sys.exit(0)
