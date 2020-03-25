

def greet():
    name = "Boris"
    print("Hello, {}".format(name))

for item in dir(greet.__code__):
    if not item.startswith("co_"):
        continue

    print(f"{item}: {getattr(greet.__code__, item)}")