#!/usr/bin/env python3

"""
# Author: Boris Gelfandbein
"""

print("### Task 1\n")

_message = str("Hello World!")
_amount  = int(12)
_fruits  = ["Apple", "Lemon", "Banana", "Peach"]

print("### Task 2\n")
if _amount >= 10:
    print(_message)
    
print("### Task 3\n")
i = 1
print(f"Total fruits: ", len(_fruits))

while i <= len(_fruits):
    for i in range(len(_fruits)):
        if i <= len(_fruits):
            print(_fruits[i], sep=',')
            i += 1
        else:
            print()
    i += 1


print("\n### Task 4")
def double_positive(_num):
    if _num > 0:
        return _num * 2
    else:
        return _num        
    
_num = int(input("Enter number to double: "))
print(f"{double_positive(_num)}\n")


print("### Task 5\n")

_num = [10, 0, 2, -7, 4]
for i in _num:
    print(double_positive(i))

print()


print("Task 6\n")
_dict = {"Alex": 17, "Nick": 8, "John": 40, "Anna": 21, "Kate": 15, "Lisa": 30, "Jake": 2}

_a = 0
_k = 0
_t = 0

for key in _dict:
    if _dict[key] >= 19:
        print(f"{key} is an adult")
        _a += 1
    elif _dict[key] <= 12:
        print(f"{key} is a kid")
        _k += 1
    else:
        print(f"{key} is a teenager")
        _t += 1

print(f"\nAdults {_a}, teenagers {_t} & kids {_k}")

    