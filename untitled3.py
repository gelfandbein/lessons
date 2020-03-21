#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 20:15:25 2020

@author: boris
"""

import subprocess
import sys

try:
    import termcolor
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", 'termcolor'])
finally:
    import termcolor

try:
    import colored
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", 'colored'])
finally:
    import colored

from random import shuffle
from string import ascii_lowercase, ascii_uppercase

def show_hint(color):
    print(colored('You length must be a number in range from 6 to 20', color))
    print(colored('Allowed difficulties: normal and hard', color))

def throw_error():
    print(colored('Error', 'red'))

def show_success_message():
    print(colored('Success', 'green'))

def validate_length(user_length):
    try:
        if 6 < int(user_length) < 20:
            return int(user_length)
        else:
            show_hint('red')
    except ValueError:
        throw_error()

def validate_difficult(user_difficult):
    if user_difficult:
        if user_difficult == 'normal' or user_difficult == 'hard':
            return user_difficult
        else:
            show_hint('red')
    else:
        throw_error()

def generate_password(length, difficult):
    numbers_list = list(range(0, length))
    letters_lowercase_list = list(ascii_lowercase)
    letters_uppercase_list = list(ascii_uppercase)
    generated_password = ''
    shuffled_list = []

    if difficult == 'hard':
        shuffled_list = numbers_list + letters_lowercase_list + letters_uppercase_list
        shuffle(shuffled_list)
        for index in range(length - 1):
            generated_password += str(shuffled_list[index])
            generated_password += '0'

        show_success_message()

        return generated_password
    elif difficult == 'normal':
        shuffle(numbers_list)
        shuffle(letters_lowercase_list)
        half_length = int(length / 2)
        for index in range(half_length):
            generated_password += str(letters_lowercase_list[index])
        for index in range(half_length):
            generated_password += str(numbers_list[index])

        show_success_message()

        return generated_password

show_hint('yellow')
input_password_length = input('How long password you want to? ')
input_password_difficult = input('Enter difficult ')

valid_length = validate_length(input_password_length)
valid_difficult = validate_difficult(input_password_difficult)

if valid_length and valid_difficult:
    result = generate_password(valid_length, valid_difficult)
    print(f'Your password = {result}')