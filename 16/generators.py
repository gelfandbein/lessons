import sys
import random
from random import shuffle

r = random.randint(1, 37)

def squares(max_num):
    for i in range(1, max_num+1):
        yield r


for x in squares(36):
    print(x)

print("Memory: ", sys.getsizeof(x))


def generate_numbers():
    nums_list = list(range(1, 37))
    for n in range(6):
        print(n)
        shuffle(nums_list)
        yield nums_list[n]

if __name__ == '__main__':
    for num in generate_numbers():
        print(num)