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
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Running time is {} seconds.'.format(end-start))
        return return_value
    return wrapper


g = '\033[92m'
y = '\033[93m'
r = '\033[91m'
b = '\033[1m'
i = '\x1B[3m'
c = '\033[0m'
u = '\033[4m'

def wrap(func):
    def wrapper(*args, **kwargs):
        print(f" ** {func()} ## ")
        print(f"{b} {func()} {c}")
    return wrapper


@wrap
def hello():
    return "Hello, world!"

p = hello()


if __name__ == "__main__":
    try:
        pass
    except KeyboardInterrupt:
        print("\nGot STOP. Turning 0FF & exiting from this f...g world...")
        sys.exit()


