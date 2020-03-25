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








if __name__ == "__main__":
    controller = TVController()
    try:
        controller.test()
        controller.main()
    except KeyboardInterrupt:
        print("\nGot STOP. Turning 0FF & exiting from this fucking world...")
        sys.exit()


