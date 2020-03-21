# def f_aaa():
#     if a > b and a > c:
#         print("Максимальное "+str(a))
#     elif b > c and b > a:
#         print("Максимальное "+str(b))
#     else:
#         print("Максимальное "+str(c))

# def f_bbb():
#     bbb = (a, b, c)
#     print(max(bbb))

# a = int(input("Введите число 1 из 3 для сравнения: "))
# b = int(input("Введите число 2 из 3 для сравнения: "))
# c = int(input("Введите число 3 из 3 для сравнения: "))

# choice = int(input("you choice?: "))

# if choice == 1:
#     f_aaa()
# elif choice == 2:
#     f_bbb()
# else:
#     pass

def _find_max_3(_a, _b, _c):
    if _a > _b > _c:
        return _a
    elif _b > _a > _c:
        return _b
    else:
        return _c

def _find_max_n(a_list):
    current_max = a_list[0]
    for i in a_list:
        if i > current_max:
            current_max = i
    return current_max

def _find_max(a_list):
    if len(a_list) == 3:
        res = _find_max_3(*a_list)
    else:
        res = _find_max_n(a_list)
    return res

def _main():
    list1 = input("enter numbers: ")
    max_value = _find_max(list1)
    print(list1, "-> max: ", max_value)

if __name__ == "__main__":
    _main()
