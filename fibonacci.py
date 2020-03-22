#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 18:50:32 2020

@author: boris
"""

"""Write a program that asks the user how many Fibonnaci numbers to
    generate and then generates them. Take this opportunity to think
    about how you can use functions. Make sure to ask the user to enter
    the number of numbers in the sequence to generate.
    (Hint: The Fibonnaci seqence is a sequence of numbers where the
    next number in the sequence is the sum of the previous two numbers
    in the sequence.
    The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

import pprint

num = int(input("Введите до какого числа считать последовательность Фибоначчи: "))


def fibonacci(num):
    fib1, fib2 = 0, 1
    for _ in range(num):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


for fib in fibonacci(num):
    print(fib, end=' ')
print()

pp = pprint.PrettyPrinter()
pp.pprint(sum(fibonacci(num)))

print("next...\n")

def fib(f):
    if f == 0:
        return 0
    if f == 1:
        return 1
    return fib(f - 1) + fib(f - 2)


a = int(input("enter num: "))
print(fib(a))
