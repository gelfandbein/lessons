###
# Создать два декоратора с именами bold и italic которые добавляют к значению,
# которое возвращает декорируемая функция символы ** и ## (в начале и конце строки) соответственно.
# Показать несколько примеров использования данных декораторов (совместно и отдельно).
# @bold
# @italic
# def hello():
#     return "Hello, world!"
# print(hello())
# Доп. задание: декорируемая функция может принимать один или несколько параметров.
# Изменить вышеприведенные декораторы для правильной обработки этой ситуации.
###

import sys
import time

def benchmark(func):
    def wrap(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Running time is {} seconds.'.format(end-start))
        return return_value
    return wrap

def decor():
    g = '\033[92m'
    y = '\033[93m'
    r = '\033[91m'
    b = '\033[1m'
    i = '\x1B[3m'
    u = '\033[4m'
    c = '\033[0m'

def symb(func):
    def wrapper(*args, **kwargs):
        print(" ** " + func() + " ## ")
    return wrapper

# def bold(func):
#     def func():
#         return Decor.s + Decor.b + h() + Decor.c + Decor.e
#     return func

# def italic(func):
#     def func():
#         return Decor.i + h() + Decor.c
#     return func

@symb
def hello():
    return "Hello, world!"

p = hello()


if __name__ == "__main__":
    try:
        pass
    except KeyboardInterrupt:
        print("\nGot STOP. Turning 0FF & exiting from this f...g world...")
        sys.exit()


