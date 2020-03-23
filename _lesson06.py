#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:53:58 2020

@author: boris
"""

my_help = """Help:
      a - add value to the list
      d - delete value from list
      r - replace value in list
      
      l - print list
      s - print sorted list
      u - print unique value
      
      h - this help text
      
      q - quit"""

print(my_help)

myList = []

while True:
    userInput = input('Введите действие: ')
    if userInput == 'l':
        for i in range(0, len(myList)):
            print(str(i) + ' - ' + myList[i])
    elif userInput == 'a':
        myList.append(input('Введите элемент списка: '))
    elif userInput == 'd':
        inputIndex = int(input('Введите индекс списка: '))
        del myList[inputIndex]
    elif userInput == 'r':
        inputIndex = int(input('Введите индекс списка: '))
        inputString = input('Введите заметку: ')
        myList[inputIndex] = inputString
    elif userInput == 'e':
        inputIndex = int(input('Введите индекс списка: '))
    elif userInput == 's':
        my_list = sorted(myList)
        print(my_list)
    elif userInput == 'u':
        uniqueMyList = set(myList)
        print(uniqueMyList)
    elif userInput == 'h':
        print(my_help)
    elif userInput == 'q':
        break