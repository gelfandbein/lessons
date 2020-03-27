
def my_decorator(func):
    print ("Я обычная функция")
    def wrapper():
        print ("Я - функция, возвращаемая декоратором")
        func()
    return wrapper

@my_decorator
def lazy_function():
    print ("zzzzzzzz")


decorated_function = my_decorator(lazy_function)
