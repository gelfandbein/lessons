# Lesson 10: Classes, scope, and namespaces
# Task 3: TV controller  
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
#
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
# The default channel turned on before all commands is №1.
#
# Your task is to create the TVController class and methods described above.
#
# ```
# CHANNELS = ["BBC", "Discovery", "TV1000"]
#
#  class TVController:
# pass
#
# controller = TVController(CHANNELS)
#
# controller.first_channel() == "BBC"
# controller.last_channel() == "TV1000"
# controller.turn_channel(1) == "BBC"
# controller.next_channel() == "Discovery"
# controller.previous_channel() == "BBC"
# controller.current_channel() == "BBC"
# controller.is_exist(4) == "No"
# controller.is_exist("BBC") == "Yes"
# """

import sys
import random

class TVController():
    def __init__(self):
        self.list = ["BBC", "Discovery", "TV1000"]
        self.status = 0
        self.channel = 0

    def test(self):
        if controller.status == 0:
            status = input("Yours TV is turned 0FF. Turn it 0N? (y/n): ")
            if status == "y":
                return print("Hardware test passed!")
            else:
                raise KeyboardInterrupt


    def swith(self, channel):
        if channel == len(controller.list):
            controller.channel = 0
        elif channel < 0:
            controller.channel = len(controller.list)-1
        
        print(f"-> '{controller.list[controller.channel]}' channel found. Switching...")
        controller.main()

    def main(self):
        print(f"Now you watch the {controller.list[controller.channel]} channel. You have {controller.list} channels.")
        choice = input("Do you want switch the channel? (p)revious or (n)ext (q - to quit): ")
        if choice == "n":
            controller.channel = controller.channel + 1
            controller.swith(controller.channel)
        elif choice == "p":
            controller.channel = controller.channel - 1
            controller.swith(controller.channel)
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
