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

import sys, random
from pynput import keyboard

class TVController():
    def __init__(self):
        pass

    def test(self):
        rnd = random.randint(0, 1)
        if rnd == 0:
            state = input("Yours TV is turned 0FF. Turn it 0N? (y/n): ")
            if state == "y":
                print("TV turned 0N!")
                return
            else:
                print("Ok! Bye bye")
                sys.exit()

        print("TV already turned 0N!")
    def channels(self):
        channels_list = ["BBC", "Discovery", "TV1000"]
        print("Channels loaded into TVController memory: ", channels_list)

    def main(self):
        print("...main block passed")
        return True



if __name__ == "__main__":
    command = int(input("Enter command: "))
    controller = TVController()
    try:
        controller.test()
        controller.channels()
        controller.main()
    except KeyboardInterrupt:
        print("\nGot KeyboardInterrupt! Exiting...")
        sys.exit()
