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


class Decor:
    def __init__(self):
        blue = '\033[94m'
        green = '\033[92m'
        yellow = '\033[93m'
        red = '\033[91m'
        bold = '\033[1m'
        italic = '\x1B[3m'
        underline = '\033[4m'
        clear = '\033[0m'
        start = ' ** '
        end = ' ## '

    def symb(self, f2d):
        return self.start + self.bold + f2d() + self.clear + self.end

    # def bold(self, f2d):
    #     def func():
    #         return self.start + self.bold + f2d() + self.clear + self.end
    #     return func

    # def italic(self, f2d):
    #     def func():
    #         return self.italic + f2d() + self.clear
    #     return func
    

@Decor.symb(hello())
#@Decor.bold
#@Decor.italic
def hello():
    return "Hello, world!"


print(hello())

if __name__ == "__main__":
    try:
        pass
    except KeyboardInterrupt:
        print("\nGot STOP. Turning 0FF & exiting from this fucking world...")
        sys.exit()


