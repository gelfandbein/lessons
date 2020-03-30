import sys
import random

a_list = ["ab", "cd", "ef"]

for w in a_list:
    print(w)

it = iter(a_list)

# print(next(it))
# print(next(it))
# print(next(it))


# list = [x*x for x in range(1_000)]
# print(list)
import sys

class Square:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.max_num:
            raise StopIteration()

        res = self.current**2
        self.current += 1
        return res

it = Square(1_000)
# for value in it:
#    print(value)

print("Mem it: ", sys.getsizeof(it))

a_list = list(it)
print("Mem it: ", sys.getsizeof(a_list))

class Enumerator:
    def __init__(self, data, start=0):
        self.data = data
        self.start = start
        self.index = self.start

    def __iter__(self):
        return self

    def __next__(self):
        try:
            idx = self.index
            self.index += 1
            return (self.get_index(idx), self.data[idx])
        except IndexError:
            raise StopIteration

    def get_index(self, base):
        return self.start + base

for x in Enumerator(["one", "two", "three"], start=0):
    print(x)

class Boss:
    def __init__(self, name, workers = []):
        self.name = name
        self.workers: list = workers
        self.worker_it = None

    def __iter__(self):
        self.worker_it = iter(self.workers)
        return self

    def __next__(self):
        return next(self.worker_it)

    def add_worker(self, name):
        self.workers.append(name)

boss = Boss("Me")

boss.add_worker("Worker 1")
boss.add_worker("Worker 2")
boss.add_worker("Worker 3")

for worker in boss:
    print(worker)

boss.add_worker("Secretary 1")
print(list(boss))


class Lotery:
    def __init__(self):
        self.numbers = list(range(37))

    def __iter__(self):
        return self

    def __next__(self):
        num = random.choice(self.numbers)
        self.numbers.remove(num)
        return num

print(Lotery())
